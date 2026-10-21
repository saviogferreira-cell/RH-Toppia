from pathlib import Path
src = Path('/sessions/admiring-ecstatic-ride/mnt/uploads/cff3e1fa-3738-4dab-8476-5673ce5a25c1-1792519810028_toppia-pre-admissoes-com-evidencia.html')
dst = Path('/sessions/admiring-ecstatic-ride/mnt/outputs/toppia-com-feedbacks.html')
s = src.read_text(encoding='utf-8')
def replace_once(old, new):
    global s
    n = s.count(old)
    assert n == 1, (old[:100], n)
    s = s.replace(old, new, 1)

style = '''
/* Feedbacks: continuidade visual da ficha, com o histórico em primeiro plano. */
.fb-summary { display:flex; align-items:flex-start; justify-content:space-between; gap:16px; flex-wrap:wrap; margin-bottom:18px; }
.fb-summary p { max-width:680px; }
.fb-picker { min-width:min(100%,300px); max-width:100%; }
.fb-overview { display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:10px; margin-top:15px; }
.fb-person { display:block; padding:16px; border:1px solid var(--border); border-radius:var(--radius); background:var(--surface); color:var(--ink); text-decoration:none; }
.fb-person:hover, .fb-person:focus-visible { border-color:var(--ink-soft); background:var(--surface-2); }
.fb-person strong { display:block; font-size:14px; }
.fb-person small { color:var(--ink-faint); display:block; margin-top:3px; }
.fb-person-meta { display:flex; justify-content:space-between; margin-top:12px; font-size:12px; color:var(--ink-soft); }
.fb-history { border-left:2px solid var(--border); margin:18px 0 0 9px; padding-left:22px; }
.fb-entry { position:relative; padding:0 0 22px; }
.fb-entry::before { content:''; position:absolute; left:-29px; top:5px; width:10px; height:10px; border-radius:50%; background:var(--ink); border:3px solid var(--surface); box-shadow:0 0 0 1px var(--border); }
.fb-entry:last-child { padding-bottom:0; }
.fb-entry-head { display:flex; justify-content:space-between; align-items:start; gap:12px; flex-wrap:wrap; margin-bottom:12px; }
.fb-entry-head h2 { font-size:16px; margin:2px 0 0; }
.fb-score { font-size:20px; font-weight:600; font-family:var(--font-mono); white-space:nowrap; }
.fb-score small { font:400 11px var(--font-ui); color:var(--ink-faint); }
.fb-competencies { display:grid; grid-template-columns:repeat(auto-fit,minmax(165px,1fr)); gap:9px; }
.fb-competency { border-top:1px solid var(--border); padding-top:8px; }
.fb-competency span { display:flex; justify-content:space-between; font-size:12px; gap:6px; }
.fb-competency .bar { margin-top:7px; }
.fb-text-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; margin-top:18px; }
.fb-text-grid h3 { margin:0 0 5px; }
.fb-text-grid p, .fb-action p { white-space:pre-wrap; overflow-wrap:anywhere; }
.fb-action { margin-top:15px; padding:13px 15px; border:1px solid var(--border); border-radius:6px; }
.fb-action h3 { margin:0 0 5px; }
.fb-action-footer { display:flex; align-items:center; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:12px; }
.fb-trend { display:flex; align-items:flex-end; gap:10px; min-height:132px; overflow-x:auto; border-bottom:1px solid var(--border); padding:4px 4px 0; }
.fb-trend-item { min-width:66px; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; gap:4px; text-align:center; font-size:11px; }
.fb-trend-bar { width:25px; background:var(--ink); border-radius:3px 3px 0 0; }
.fb-trend-item time { color:var(--ink-faint); white-space:nowrap; }
.fb-form-scores { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; }
.fb-form-scores .field { margin:0; }
.field textarea { width:100%; min-height:70px; border:1px solid var(--border); border-radius:6px; padding:8px 10px; font:13px var(--font-ui); background:var(--bg); color:var(--ink); resize:vertical; }
.fb-modal { max-width:660px; }
@media(max-width:640px) { .fb-text-grid, .fb-form-scores { grid-template-columns:1fr; } .fb-summary .btn { width:100%; } .fb-picker { width:100%; } }
'''
replace_once('</style>', style + '\n</style>')
replace_once('  DB.movements = DB.movements || [];', '  DB.movements = DB.movements || [];\n  DB.feedbacks = DB.feedbacks || [];')
replace_once("  Administrador: ['dashboard', 'pendencias', 'admissoes', 'colaboradores', 'contratados', 'documentos', 'tip',", "  Administrador: ['dashboard', 'pendencias', 'admissoes', 'colaboradores', 'feedbacks', 'contratados', 'documentos', 'tip',")
replace_once("  'RH Administrador': ['dashboard', 'pendencias', 'admissoes', 'colaboradores', 'contratados', 'documentos', 'tip',", "  'RH Administrador': ['dashboard', 'pendencias', 'admissoes', 'colaboradores', 'feedbacks', 'contratados', 'documentos', 'tip',")
replace_once("  Gestor: ['dashboard', 'pendencias', 'colaboradores', 'ferias',", "  Gestor: ['dashboard', 'pendencias', 'colaboradores', 'feedbacks', 'ferias',")
replace_once("  { id: 'contratados', label: 'Prestadores PJ', icon: '⛁', group: 'Pessoas' },", "  { id: 'contratados', label: 'Prestadores PJ', icon: '⛁', group: 'Pessoas' },\n  { id: 'feedbacks', label: 'Feedbacks', icon: '◉', group: 'Desenvolvimento & SST' },")
replace_once("  const vig = L.salarioVigente(e.id, REF, DB.salaryHistory);\n  const hist = DB.salaryHistory.filter(h => h.employeeId === e.id)", "  const vig = L.salarioVigente(e.id, REF, DB.salaryHistory);\n  const hist = DB.salaryHistory.filter(h => h.employeeId === e.id)") # assert anchor
replace_once("    ${openOff ? `<section class=\"panel\" style=\"margin-bottom:16px;\"><h2>Desligamento em andamento</h2>${offboardingChecklistHtml(openOff)}</section>` : ''}\n\n    <div class=\"two-col\">", "    ${openOff ? `<section class=\"panel\" style=\"margin-bottom:16px;\"><h2>Desligamento em andamento</h2>${offboardingChecklistHtml(openOff)}</section>` : ''}\n\n    ${ROLE_MENU[SESSION.role].includes('feedbacks') ? `<section class=\"panel\" style=\"margin-bottom:16px;\"><h2>Feedbacks e evolução</h2><p>${DB.feedbacks.filter(f => Number(f.employeeId) === Number(e.id)).length} avaliação(ões) registrada(s). Consulte as competências, o histórico e os planos de ação.</p><a class=\"btn\" href=\"#/feedbacks/${e.id}\">Ver evolução de ${escapeHtml(e.nome)}</a></section>` : ''}\n\n    <div class=\"two-col\">")

feature = r'''
/* ===================== FEEDBACK E EVOLUÇÃO ===================== */
const FB_COMPETENCIES = [
  { key:'entrega', label:'Entrega e qualidade' },
  { key:'colaboracao', label:'Colaboração' },
  { key:'comunicacao', label:'Comunicação' },
  { key:'iniciativa', label:'Iniciativa' },
  { key:'desenvolvimento', label:'Aprendizado' }
];
function feedbackScore(f) {
  const vals = FB_COMPETENCIES.map(c => Number((f.scores || {})[c.key]));
  return vals.every(n => Number.isInteger(n) && n >= 1 && n <= 5) ? vals.reduce((a,b) => a+b, 0) / vals.length : null;
}
function feedbackDates() { return new Date().toLocaleDateString('en-CA'); }
function feedbackEmployee(id) { return visibleEmployees().find(e => String(e.id) === String(id)); }
function feedbackEntries(id) {
  return DB.feedbacks.filter(f => Number(f.employeeId) === Number(id))
    .slice().sort((a,b) => b.data.localeCompare(a.data) || b.id - a.id);
}
function feedbackOverview() {
  const employees = visibleEmployees().slice().sort((a,b) => a.nome.localeCompare(b.nome, 'pt-BR'));
  if (!employees.length) return `<div class="empty">${isGestorScoped() ? 'Selecione um gestor no topo para ver a equipe.' : 'Nenhum colaborador cadastrado.'}</div>`;
  return `<div class="fb-overview">${employees.map(e => {
    const entries = feedbackEntries(e.id), last = entries[0], score = last && feedbackScore(last);
    return `<a class="fb-person" href="#/feedbacks/${e.id}"><strong>${escapeHtml(e.nome)}</strong>
      <small>${escapeHtml(e.cargo || 'Cargo não informado')} · ${escapeHtml(e.departamento || 'Sem departamento')}</small>
      <span class="fb-person-meta"><span>${entries.length} avaliação(ões)</span><span>${score == null ? 'Sem nota' : score.toFixed(1) + ' / 5'}${last ? ` · ${L.fmtDateBR(last.data)}` : ''}</span></span></a>`;
  }).join('')}</div>`;
}
VIEWS.feedbacks = function(id) {
  const employee = id ? feedbackEmployee(id) : null;
  if (id && !employee) return `<div class="empty">Colaborador não encontrado ou fora da equipe selecionada.</div>`;
  if (!employee) return `<div class="page-head"><h1>Feedbacks</h1><p>Histórico de avaliações por competências e acompanhamento dos planos de ação.</p></div>
    <section class="panel"><h2>Colaboradores</h2><p>Selecione uma pessoa para registrar um feedback ou consultar sua evolução.</p>${feedbackOverview()}</section>`;
  const records = feedbackEntries(employee.id), chronological = records.slice().reverse();
  const firstScore = chronological.length ? feedbackScore(chronological[0]) : null;
  const lastScore = records.length ? feedbackScore(records[0]) : null;
  const delta = firstScore != null && lastScore != null && records.length > 1 ? lastScore - firstScore : null;
  const pending = records.filter(f => f.plano && f.actionStatus !== 'Concluído').length;
  const trend = chronological.map(f => {
    const score = feedbackScore(f);
    return `<div class="fb-trend-item" title="${L.fmtDateBR(f.data)}: ${score == null ? 'sem nota' : score.toFixed(1) + ' de 5'}"><strong>${score == null ? '—' : score.toFixed(1)}</strong>
      <div class="fb-trend-bar" style="height:${score == null ? 3 : Math.round(score * 16)}px"></div><time datetime="${f.data}">${L.fmtDateBR(f.data)}</time></div>`;
  }).join('');
  const history = records.map(f => {
    const score = feedbackScore(f), pendingAction = f.plano && f.actionStatus !== 'Concluído';
    const scores = FB_COMPETENCIES.map(c => {
      const n = Number((f.scores || {})[c.key]);
      return `<div class="fb-competency"><span><span>${c.label}</span><strong>${n || '—'} / 5</strong></span><div class="bar"><div class="bar-fill bar-ok" style="width:${n ? n*20 : 0}%"></div></div></div>`;
    }).join('');
    return `<div class="fb-entry"><article class="panel"><div class="fb-entry-head"><div><time class="muted" datetime="${f.data}">${L.fmtDateBR(f.data)}</time>
      <h2>${escapeHtml(f.tipo || 'Feedback periódico')}</h2><p>Responsável: ${escapeHtml(f.autor || 'Não informado')}</p></div>
      <div class="fb-score">${score == null ? '—' : score.toFixed(1)} <small>/ 5 · média das competências</small></div></div>
      <div class="fb-competencies">${scores}</div>
      <div class="fb-text-grid"><div><h3>Pontos fortes</h3><p>${escapeHtml(f.pontosFortes)}</p></div><div><h3>Oportunidades de melhoria</h3><p>${escapeHtml(f.melhorias)}</p></div></div>
      ${f.plano ? `<div class="fb-action"><h3>Plano de ação</h3><p>${escapeHtml(f.plano)}</p><div class="fb-action-footer"><span>Prazo: ${f.prazo ? L.fmtDateBR(f.prazo) : 'sem prazo'} · ${badge(f.actionStatus || 'Em andamento', pendingAction ? 'warn' : 'ok')}</span>
        ${pendingAction ? `<button class="btn" data-action="concluir-feedback" data-id="${f.id}">Concluir ação</button>` : ''}</div>
        ${f.actionUpdates && f.actionUpdates.length ? `<p class="muted" style="font-size:12px; margin:9px 0 0">${f.actionUpdates.map(u => `${L.fmtDateBR(u.data)} · ${escapeHtml(u.nota)}`).join('<br>')}</p>` : ''}</div>` : ''}
      <p class="muted" style="font-size:11px; margin-top:14px;">Registrado em ${escapeHtml(f.criadoEm || f.data)} · registro #${f.id}</p>
    </article></div>`;
  }).join('');
  return `<div class="page-head"><a href="#/feedbacks" class="breadcrumb">← Feedbacks</a>
    <div class="fb-summary"><div><h1>${escapeHtml(employee.nome)}</h1><p>${escapeHtml(employee.cargo || '')} · ${escapeHtml(employee.departamento || 'Sem departamento')} · ${records.length} avaliação(ões) registradas</p></div>
      <button class="btn btn-primary" data-action="novo-feedback" data-id="${employee.id}">+ Registrar feedback</button></div></div>
    <div class="kpi-grid">${card('Última avaliação', lastScore == null ? '—' : lastScore.toFixed(1) + ' / 5', records[0] ? L.fmtDateBR(records[0].data) : 'Ainda não avaliado')}
      ${card('Evolução desde a primeira', delta == null ? '—' : (delta >= 0 ? '+' : '') + delta.toFixed(1), records.length > 1 ? 'Pontos na média das competências' : 'É preciso registrar ao menos duas avaliações')}
      ${card('Planos em andamento', pending, 'Ações de feedback ainda não concluídas')}</div>
    ${records.length ? `<section class="panel"><h2>Evolução das avaliações</h2><p class="muted">Média simples das cinco competências, escala de 1 a 5. Compare também cada competência no histórico abaixo.</p><div class="fb-trend">${trend}</div></section>
      <h2 style="margin:22px 0 14px">Histórico de feedbacks</h2><div class="fb-history">${history}</div>` : `<section class="panel"><h2>Sem feedbacks registrados</h2><p>Registre a primeira avaliação para começar a acompanhar a evolução de ${escapeHtml(employee.nome)}.</p>
      <button class="btn btn-primary" data-action="novo-feedback" data-id="${employee.id}">Registrar primeiro feedback</button></section>`}`;
};
ACTIONS['novo-feedback'] = (id) => {
  const emp = feedbackEmployee(id);
  if (!emp || !ROLE_MENU[SESSION.role].includes('feedbacks')) return;
  const scoreFields = FB_COMPETENCIES.map(c => `<label class="field"><span>${c.label} *</span><select name="score_${c.key}" required>
    <option value="">Selecione a nota</option>${[1,2,3,4,5].map(n => `<option value="${n}">${n} / 5</option>`).join('')}</select></label>`).join('');
  openModal(`Novo feedback — ${escapeHtml(emp.nome)}`, `
    <p class="muted">Avalie de 1 (precisa desenvolver) a 5 (destaque). O registro permanece no histórico do colaborador.</p>
    <label class="field"><span>Data da conversa *</span><input name="data" type="date" value="${feedbackDates()}" required></label>
    <label class="field"><span>Tipo *</span><select name="tipo" required><option value="Periódico">Periódico</option><option value="Acompanhamento">Acompanhamento</option><option value="Reconhecimento">Reconhecimento</option><option value="Desenvolvimento">Desenvolvimento</option></select></label>
    <label class="field"><span>Responsável pelo feedback *</span><input name="autor" type="text" maxlength="120" required placeholder="Nome de quem conduziu a conversa"></label>
    <h3>Competências</h3><div class="fb-form-scores">${scoreFields}</div>
    <label class="field"><span>Pontos fortes *</span><textarea name="pontosFortes" maxlength="2000" required placeholder="Comportamentos e resultados observados"></textarea></label>
    <label class="field"><span>Oportunidades de melhoria *</span><textarea name="melhorias" maxlength="2000" required placeholder="O que pode ser desenvolvido"></textarea></label>
    <label class="field"><span>Plano de ação</span><textarea name="plano" maxlength="2000" placeholder="Ação concreta e como acompanhar"></textarea></label>
    <label class="field"><span>Prazo da ação (se houver plano)</span><input name="prazo" type="date"></label>
  `, d => {
    const scores = Object.fromEntries(FB_COMPETENCIES.map(c => [c.key, Number(d['score_' + c.key])]));
    if (Object.values(scores).some(n => !Number.isInteger(n) || n < 1 || n > 5)) { alert('Selecione notas de 1 a 5 para todas as competências.'); return false; }
    if (!d.data || !d.autor.trim() || !d.pontosFortes.trim() || !d.melhorias.trim()) { alert('Preencha data, responsável, pontos fortes e melhorias.'); return false; }
    if (d.prazo && !d.plano.trim()) { alert('Informe um plano de ação para definir um prazo.'); return false; }
    DB.feedbacks.push({ id:nextId('feedbacks'), employeeId:emp.id, data:d.data, tipo:d.tipo, autor:d.autor.trim(),
      scores, pontosFortes:d.pontosFortes.trim(), melhorias:d.melhorias.trim(), plano:d.plano.trim(),
      prazo:d.prazo || null, actionStatus:d.plano.trim() ? 'Em andamento' : null, actionUpdates:[], criadoEm:new Date().toISOString() });
    location.hash = '#/feedbacks/' + emp.id;
  });
  document.querySelector('#modal-root .modal').classList.add('fb-modal');
};
ACTIONS['concluir-feedback'] = id => {
  const f = DB.feedbacks.find(item => String(item.id) === String(id));
  if (!f || !feedbackEmployee(f.employeeId) || !ROLE_MENU[SESSION.role].includes('feedbacks') || !f.plano || f.actionStatus === 'Concluído') return;
  openModal('Concluir plano de ação', `<p class="muted">Registre o resultado da ação para manter o acompanhamento no histórico.</p>
    <label class="field"><span>Data da conclusão *</span><input type="date" name="data" value="${feedbackDates()}" required></label>
    <label class="field"><span>Resultado / evidência *</span><textarea name="nota" maxlength="2000" required></textarea></label>`, d => {
    if (!d.data || !d.nota.trim()) { alert('Preencha a data e o resultado da ação.'); return false; }
    f.actionUpdates = f.actionUpdates || [];
    f.actionUpdates.push({ data:d.data, nota:d.nota.trim(), status:'Concluído' });
    f.actionStatus = 'Concluído';
  });
};
'''
replace_once("document.addEventListener('DOMContentLoaded', () => {\n  loadDB();", feature + "\ndocument.addEventListener('DOMContentLoaded', () => {\n  loadDB();")
replace_once('Recrutamento e Seleção, Avaliação de Desempenho, assinatura eletrônica real,', 'Recrutamento e Seleção, avaliação de desempenho com autenticação e compartilhamento em servidor, assinatura eletrônica real,')
dst.write_text(s, encoding='utf-8')
print(dst, len(s), 'bytes')
