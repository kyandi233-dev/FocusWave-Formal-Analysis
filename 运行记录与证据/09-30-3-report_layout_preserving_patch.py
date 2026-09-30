#!/usr/bin/env python3
"""Apply audited report edits without reserializing the Word document package.

Only text-node contents and four explicitly renumbered SEQ instructions change.
Unchanged OOXML parts and retained body elements are copied byte for byte.
Seven redundant tables are removed; all four original sections are retained.
"""
from __future__ import annotations
import argparse, copy, csv, difflib, hashlib, html, json, re, zipfile
from pathlib import Path
from xml.parsers import expat
from lxml import etree as ET

NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W='{'+NS['w']+'}'
EXPECTED='8830a3e11cca3ca1357b0311c420a5921b9d0a318e1e4d2d36b4b0a8fd5ae1e0'
TEXT_RE=re.compile(rb'(<w:t(?:\s[^>]*)?>)(.*?)(</w:t>)',re.S)

def sha(data:bytes)->str: return hashlib.sha256(data).hexdigest()
def text(data:bytes)->str:
    return ''.join(html.unescape(m.group(2).decode('utf-8')) for m in TEXT_RE.finditer(data))

def body_ranges(data:bytes):
    """Exact byte ranges for direct w:body children, including nested tables."""
    parser=expat.ParserCreate(); stack=[]; ranges=[]; start=None
    def enter(name,attrs):
        nonlocal start
        if stack and stack[-1]=='w:body': start=parser.CurrentByteIndex
        stack.append(name)
    def leave(name):
        nonlocal start
        if len(stack)>=2 and stack[-2]=='w:body':
            at=parser.CurrentByteIndex
            if data[at:at+2]==b'</': end=data.index(b'>',at)+1
            else: end=at
            ranges.append((start,end));start=None
        stack.pop()
    parser.StartElementHandler=enter;parser.EndElementHandler=leave;parser.Parse(data,True)
    return ranges

def replace_text(data:bytes,old:str,new:str)->bytes:
    """Surgical character diff: preserve equal text and every existing run property."""
    before=text(data)
    if before.count(old)!=1:
        raise ValueError(f'Expected one match, found {before.count(old)}: {old[:100]}')
    after=before.replace(old,new,1)
    matches=list(TEXT_RE.finditer(data));values=[html.unescape(m.group(2).decode()) for m in matches]
    owner=[]
    for k,v in enumerate(values):owner.extend([k]*len(v))
    output=['']*len(values)
    for tag,i,j,a,b in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
        if tag=='equal':
            for pos,ch in zip(range(i,j),after[a:b]):output[owner[pos]]+=ch
        elif tag in ('replace','insert'):
            target=owner[i] if i<len(owner) else owner[-1]
            output[target]+=after[a:b]
    changed=[]
    for m,o,n in zip(matches,values,output):
        if o!=n:changed.append((m.start(2),m.end(2),html.escape(n,quote=False).encode('utf-8')))
    for a,b,v in reversed(changed):data=data[:a]+v+data[b:]
    assert text(data)==after
    return data

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--audit-dir',type=Path,required=True)
    args=ap.parse_args(); raw=args.input.read_bytes(); assert sha(raw)==EXPECTED,'Wrong original version'
    z=zipfile.ZipFile(args.input);original=z.read('word/document.xml');ranges=body_ranges(original)
    chunks=[original[a:b] for a,b in ranges];old_chunks=list(chunks)
    root=ET.fromstring(original);body=root.find('w:body',NS)
    assert len(chunks)==len(body)==768
    p_indices=[i for i,e in enumerate(body) if e.tag==W+'p']
    log=[]
    def change(i,old,new,reason):
        b=text(chunks[i]);chunks[i]=replace_text(chunks[i],old,new)
        log.append({'original_body_index':i,'kind':'text','reason':reason,'before':b,'after':text(chunks[i])})
    def para(p,old,new,reason):change(p_indices[p],old,new,reason)
    def whole(i,new,reason):change(i,text(chunks[i]),new,reason)
    # Scientific citation corrections, with the original author emphasis preserved.
    para(37,'目标事件出现频率、目标与非目标的辨别难度以及任务结构都会影响警觉递减的程度',
         '刺激呈现速率、辨别方式与记忆要求会影响警觉递减的程度',
         'See 1995 original abstract: event rate is stimulus presentation rate; successive/simultaneous discrimination')
    para(57,'行为研究也提供了相应支持。','行为研究进一步考察了探针报告与近期任务表现的对应。',
         'Bastian 2013: association with thought reports, not separate validation of every content category')
    para(58,'总结了多种探针设计，指出题干、选项设置和报告要求都会影响测量结果',
         '总结了多种探针设计，梳理题干、选项设置和报告要求等测量差异，并讨论不同设计之间的可比性',
         'Weinstein 2018: methods review does not establish a universal causal effect')
    para(58,'其他研究发现，探针频率或提问方式改变后，行为表现与主观报告的变化方式可能有所不同（Robison et al., 2019）。',
         'Robison 等（2019）在三项实验中未发现探针频率和提问框架影响行为表现或探针回答，并强调应在选项中区分任务聚焦、任务外思维和任务相关干扰。',
         'Robison 2019: restore the direction and scope of the actual findings')
    para(73,'重新睁眼前后还可能出现测量异常。同时，眨眼本身可伴随持续一段时间的真实瞳孔变化（Mathôt et al., 2018; Kret & Sjak-Shie, 2019; Yoo et al., 2021）。',
         '重新睁眼前后还可能出现测量异常（Mathôt et al., 2018; Kret & Sjak-Shie, 2019）。同时，眨眼本身可伴随持续一段时间的真实瞳孔变化（Yoo et al., 2021）。',
         'Separate preprocessing sources from the source of blink-related physiological pupil changes')
    para(78,'但执行控制指标并没有出现同样程度的变化','而两类执行控制指标均未检出姿态效应',
         'Qian 2024: two executive-control measures showed no detected posture effect')
    para(79,'Bosch 和 D’Mello（2021）利用上半身动作、头部姿态和面部信息预测思维探针报告，在实验室和课堂数据中都获得了高于随机水平的预测表现。',
         'Bosch 和 D’Mello（2021）在实验室阅读中利用上半身动作、头部姿态和面部信息，在课堂学习中实时提取头部姿态与面部动作特征，两种情境下的心智游移预测均高于随机水平。',
         'Bosch 2021: distinguish lab video inputs from real-time classroom head-pose/facial features')
    # Locate the original system comparison table by exact content.
    idx=[i for i,c in enumerate(chunks) if '阅读中的眼动、皮电与行为信息' in text(c)];assert len(idx)==1
    change(idx[0],'阅读中的眼动、皮电与行为信息','阅读中的眼动与皮电信息',
           'Brishtel 2020: actual automated classifier inputs')
    para(536,'Estraneo, A., Trojano, L., & Conson, M.','Estraneo, A., & Trojano, L.',
         'Magliacano 2020: remove incorrectly added fifth author')
    para(541,'Salinsky, M.,','Salinsky, M. C.,','Oken 2006: complete author initials')
    para(544,'Sgreccia, G.,','Sgreccia, D.,','Paterniani 2023: correct author initial')
    change(689,'判别力 β（对数线性）','反应偏向 β（对数线性）','Restore the meaning of beta; estimates unchanged')
    # Seven redundant tables. Retain the original wide A3 and F2 rather than rebuilding them.
    deleted=set(range(614,622))|set(range(637,642))|{684,685}|set(range(697,701))|set(range(723,727))|set(range(730,735))|set(range(742,747))|{753,754}|set(range(756,761))
    assert sum(body[i].tag==W+'tbl' for i in deleted)==7
    assert not any(body[i].xpath('.//w:sectPr',namespaces=NS) for i in deleted)
    whole(613,'本附录对应正文 5.9，补充事后问卷有序模型的完整系数、估计精度，以及与探针前分析不同的反应时筛选条件。',
          'Keep supplementary information rather than repeat the main-text sample and result summary')
    change(622,'A.3','A.1','Synchronize appendix subsection numbering')
    change(623,'因变量为 A.2 所列三级有序变量','因变量为正文 5.9 所列三级走神比例','Update cross-reference after removing duplicate distribution table')
    change(631,'A.4','A.2','Synchronize appendix subsection numbering')
    # Caption text and native fields are both retained and renumbered together.
    for i,old,new,n in [(632,'表 A3','表 A1',1),(737,'表 E2','表 E1',1),(749,'表 E4','表 E2',2),(763,'表 F2','表 F1',1)]:
        change(i,old,new,'Renumber retained native Word caption')
        chunks[i],count=re.subn(rb'(SEQ\s+[^<]*?\\r\s+)\d+',lambda m:m.group(1)+str(n).encode(),chunks[i])
        assert count==1
    whole(643,'本附录按任务进程、主观注意、同期行为与跨参与者预测，呈现眼部信息在不同测量层面的完整结果。参与者内关联描述同一人相对自身平均水平的变化，参与者间关联描述个体平均水平的差异。模型比较同时呈现预测损失、区分能力与相应不确定性，补充正文对各类信息价值的分析。',
          'Judge-facing synthesis of the appendix structure and scientific comparison levels')
    change(683,'附录 F 与本表采用同一结果来源。','模型的布里尔分数、单一类别人数与校准斜率见附录 F。',
           'Explain the distinct contribution of the retained landscape probability table')
    whole(701,'补充行为指标中，正确反应时的均值、标准差、四分位距和中位数绝对偏差均可在 2318 个探针前窗口内计算；辨别力、筛选后遗漏及存在时序歧义的遗漏均为 2320 个窗口，涉及 61 名参与者、116 个场次。',
          'Preserve unique coverage of supplementary metrics after removing duplicated coverage table')
    change(718,'（正式伴随结果）','','Remove internal result-status wording from the judge-facing heading')
    whole(727,'动作指标及曝光变化、全画面运动和平均灰度均覆盖 61 名参与者的 115 个场次、2300 个探针（99.14%）。整体动作强度用于主要分析；横向、纵向与前后方向用于姿态补充分析，曝光变化、全画面运动和平均灰度用于评价成像质量。',
          'Compress repeated coverage while retaining scientific roles of supplementary and quality measures')
    whole(729,'本附录对应正文 5.5，比较同步心电对照中的误差类型与心率估计方法，为理解毫米波心肺测量的表现及其改进方向提供依据。',
          'Describe the purpose of the appendix instead of repeating coverage')
    change(735,'E.2','E.1','Synchronize appendix subsection numbering')
    change(748,'E.4','E.2','Synchronize appendix subsection numbering')
    whole(747,'排除谐波类之后，其余探针平均误差为 −6.765 次/min，说明波峰识别与通道选择也共同影响总体低估。',
          'Retain the unique error-exclusion finding without a redundant derived-contribution table')
    change(755,'监督学习完整结果附表','模型概率诊断','Name the unique content retained in Appendix F')
    change(762,'F.2','F.1','Synchronize appendix subsection numbering')
    change(766,'该诊断用于描述完成预测后的概率表现。','布里尔分数反映概率预测误差，校准斜率用于评价预测概率与实际报告之间的对应。',
           'Explain the scientific purpose of probability diagnostics without engineering narration')
    # New figure note uses one existing original note paragraph as an exact formatting donor.
    fig4=[i for i,c in enumerate(chunks) if text(c)=='图 4 专注预测与系统解释'];assert len(fig4)==1
    donor=[i for i,c in enumerate(chunks) if text(c).startswith('注：预实验被试与多模态采集设备布置示意')];assert len(donor)==1
    note=replace_text(chunks[donor[0]],text(chunks[donor[0]]),
        '注：本图展示独立预测、行为增量与条件预测三类比较设计，柱形用于说明比较关系；实测表现见第 5.6—5.8 节。')
    # IDs/bookmarks in a cloned note must not duplicate document identity; rPr/pPr are untouched.
    note=re.sub(rb'\s(?:w14:paraId|w14:textId|w:rsidR|w:rsidRDefault|w:rsidP)="[^"]*"',b'',note,count=0)
    note=re.sub(rb'<w:bookmarkStart\b[^>]*/>|<w:bookmarkEnd\b[^>]*/>',b'',note)
    log.append({'original_body_index':fig4[0],'kind':'note','reason':'Clarify an illustrative diagram in a positive judge-facing explanation','before':'','after':text(note)})
    # Keep all four original section properties. Appendix F title belongs on its original landscape table page.
    order=[i for i in range(len(chunks)) if i not in deleted and i!=755]
    order.insert(order.index(762),755)
    out=[]
    for i in order:
        out.append(chunks[i])
        if i==fig4[0]:out.append(note)
    new_xml=original[:ranges[0][0]]+b''.join(out)+original[ranges[-1][1]:]
    nr=ET.fromstring(new_xml);nb=nr.find('w:body',NS)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(args.output,'w') as dest:
        for info in z.infolist():dest.writestr(copy.copy(info),new_xml if info.filename=='word/document.xml' else z.read(info.filename))
    oz=zipfile.ZipFile(args.output)
    assert all(z.read(n)==oz.read(n) for n in z.namelist() if n!='word/document.xml')
    assert z.namelist()==oz.namelist()
    assert len(nr.xpath('//w:sectPr',namespaces=NS))==4
    for a,b in zip(root.xpath('//w:sectPr',namespaces=NS),nr.xpath('//w:sectPr',namespaces=NS)):
        assert ET.tostring(a)==ET.tostring(b)
    assert len(nb.findall('w:tbl',NS))==41
    assert len(nr.xpath('//w:instrText[contains(text(),"SEQ")]',namespaces=NS))==79
    # Assert all retained element formatting and non-text internals are identical, except SEQ resets.
    format_failures=[];modified=[]
    def format_skeleton(blob):
        blob=TEXT_RE.sub(lambda m:m.group(1)+b'__TEXT__'+m.group(3),blob)
        blob=re.sub(rb'(<w:instrText[^>]*>).*?(</w:instrText>)',rb'\1__FIELD__\2',blob,flags=re.S)
        return blob
    for i in order:
        if chunks[i]!=old_chunks[i]:modified.append(i)
        if format_skeleton(chunks[i])!=format_skeleton(old_chunks[i]):format_failures.append(i)
    assert not format_failures,format_failures
    for i in deleted:
        log.append({'original_body_index':i,'kind':'delete','reason':'Duplicate table or repeated annex explanation','before':text(old_chunks[i]),'after':''})
    # Figures and their native captions are unchanged byte-for-byte.
    figures=[i for i,e in enumerate(body) if e.xpath('.//w:drawing',namespaces=NS)]
    figcaps=[i for i,c in enumerate(old_chunks) if re.match(r'^图 \d+ ',text(c))]
    assert len(figcaps)==39
    assert all(chunks[i]==old_chunks[i] and i in order for i in figures+figcaps)
    retained_tables=[i for i,e in enumerate(body) if e.tag==W+'tbl' and i in order]
    unchanged_tables=[i for i in retained_tables if old_chunks[i]==chunks[i]]
    # Experimental numeric fields in every retained table are identical.
    num_re=re.compile(r'(?<!\w)[−-]?\d*\.?\d+(?:[eE][−+-]?\d+)?')
    assert all(num_re.findall(text(old_chunks[i]))==num_re.findall(text(chunks[i])) for i in retained_tables)
    a_rows=body[681].findall('w:tr',NS);f_rows=body[758].findall('w:tr',NS)
    def cells(row):return [''.join(e.xpath('.//w:t/text()',namespaces=NS)) for e in row.findall('w:tc',NS)]
    assert len(a_rows)==len(f_rows)==57
    for ar,fr in zip(a_rows[1:],f_rows[1:]):
        a,f=cells(ar),cells(fr)
        assert a[0]==f[1]
        assert a[1]==f[2]+'/'+f[3]
        assert a[2]==f[4]
        assert re.findall(r'[-−]?\d+\.\d+',a[3])==[f[5],f[6]]
    report={'status':'PASS','input_name':args.input.name,'input_sha256':sha(raw),'output_name':args.output.name,'output_sha256':sha(args.output.read_bytes()),
      'archive_members':len(z.namelist()),'unchanged_archive_members':len(z.namelist())-1,'changed_archive_members':['word/document.xml'],
      'original_body_children':len(body),'output_body_children':len(nb),'original_paragraphs':len(body.findall('w:p',NS)),'output_paragraphs':len(nb.findall('w:p',NS)),
      'original_tables':48,'output_tables':41,'retained_tables_byte_identical':len(unchanged_tables),
      'retained_table_numeric_content_unchanged':True,'original_sections':4,'output_sections':4,'all_section_properties_identical':True,
      'original_native_captions':86,'output_native_captions':79,'all_39_figure_captions_byte_identical':True,
      'modified_body_indices':modified,'deleted_body_indices':sorted(deleted),'appendix_F_title_moved_with_original_format':True,
      'format_skeleton_failures':format_failures,'duplicate_B9_F1_rows_verified':56,'retained_annexes':['A','B','C','D','E','F'],
      'all_media_byte_identical':True,'new_figure_note_format_donor_original_body_index':donor[0],
      'body_formatting_changes':0,'model_retrains':0,'raw_analysis_reruns':0,
      'render_verification':'PENDING'}
    args.audit_dir.mkdir(parents=True,exist_ok=True)
    (args.audit_dir/'format_integrity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    (args.audit_dir/'text_change_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf8')
    with (args.audit_dir/'text_change_log.csv').open('w',encoding='utf-8-sig',newline='') as f:
        cw=csv.DictWriter(f,fieldnames=['original_body_index','kind','reason','before','after']);cw.writeheader();cw.writerows(log)
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
