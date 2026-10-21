from pathlib import Path
src = Path('/sessions/admiring-ecstatic-ride/mnt/outputs/toppia-com-feedbacks.html')
out = Path('/sessions/admiring-ecstatic-ride/mnt/outputs/toppia-corrigido.html')
s = src.read_text(encoding='utf-8')
def replace_once(old, new):
    global s
    n = s.count(old)
    assert n == 1, (old[:150], n)
    s = s.replace(old, new, 1)

# Do not change the BASE_VERSION or STORAGE_KEY: existing local edits and feedbacks must survive.
replace_once("""      const result = await onSubmit(data);
      if (result === false) { if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Salvar'; } return; } // onSubmit pode devolver false para manter o modal aberto (ex.: erro de validação já avisado)
      close();
      saveDB();
      render();
    } catch (err) {
      console.error(err);
      alert('Não foi possível concluir: ' + (err && err.message ? err.message : err));
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Salvar'; }
""", """      if (!modalForm.dataset.awaitingSave) {
        const result = await onSubmit(data);
        if (result === false) { if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Salvar'; } return; }
        // Se o armazenamento falhar, não execute onSubmit duas vezes ao tentar salvar novamente.
        modalForm.dataset.awaitingSave = 'true';
      }
      saveDB();
      close();
      render();
    } catch (err) {
      console.error(err);
      alert('Não foi possível salvar: ' + (err && err.message ? err.message : err));
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = modalForm.dataset.awaitingSave ? 'Tentar salvar novamente' : 'Salvar'; }
""")
replace_once("""function saveDB() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(DB)); } catch (e) { /* quota etc */ }
}
""", """// Uma gravação com erro NÃO é confirmação de salvamento. Os dados continuam em memória
// nesta aba até que o usuário tente novamente; fechar ou recarregar pode perdê-los.
let UNSAVED_CHANGES = false;
function showSaveWarning() {
  if (typeof document === 'undefined' || !document.body) return;
  let warning = document.getElementById('save-warning');
  if (warning) return;
  warning = document.createElement('div');
  warning.id = 'save-warning';
  warning.setAttribute('role', 'alert');
  warning.style.cssText = 'position:fixed;left:12px;right:12px;bottom:12px;z-index:100;background:#FFF3C4;color:#242012;border:2px solid #A17F00;border-radius:8px;padding:12px 16px;box-shadow:0 8px 30px rgba(0,0,0,.35);font:14px/1.5 sans-serif;';
  warning.innerHTML = '<strong>Alterações não salvas.</strong> Os dados continuam nesta aba, mas serão perdidos se ela for fechada. Libere espaço ou permita o armazenamento no navegador e tente novamente. <button type="button" id="retry-save" style="margin-left:8px;padding:6px 10px;cursor:pointer">Tentar salvar</button>';
  document.body.appendChild(warning);
  warning.querySelector('#retry-save').addEventListener('click', () => {
    try { saveDB(); document.getElementById('modal-root').innerHTML = ''; render(); }
    catch (err) { alert('Ainda não foi possível salvar: ' + err.message); }
  });
}
function saveDB() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(DB));
    UNSAVED_CHANGES = false;
    const warning = document.getElementById('save-warning');
    if (warning) warning.remove();
  } catch (e) {
    UNSAVED_CHANGES = true;
    showSaveWarning();
    throw new Error('O navegador recusou a gravação. Suas alterações estão apenas na aba aberta; não recarregue nem feche a página. Use “Tentar salvar” após liberar espaço ou habilitar o armazenamento.');
  }
}
window.addEventListener('beforeunload', (event) => {
  if (!UNSAVED_CHANGES) return;
  event.preventDefault();
  event.returnValue = '';
});
""")
replace_once("""function resetDB() {
  localStorage.removeItem(STORAGE_KEY);
  loadDB();
  render();
}
""", """function resetDB() {
  // Remover dados locais com armazenamento bloqueado não pode parecer uma restauração bem-sucedida.
  localStorage.removeItem(STORAGE_KEY);
  UNSAVED_CHANGES = false;
  const warning = document.getElementById('save-warning');
  if (warning) warning.remove();
  loadDB();
  render();
}
""")
replace_once("""    openModal(`Avançar: ${a.stage} → ${proxima}`, `
      <p class="muted">Registre o que foi feito nesta etapa ou informe uma referência de evidência. O arquivo em si não é armazenado neste protótipo.</p>
""", """    openModal(`Avançar: ${a.stage} → ${proxima}`, `
      <p class="muted">Registre o que foi feito nesta etapa ou informe uma referência de evidência. O arquivo em si não é armazenado neste protótipo.</p>
      ${proxima === 'Ativo' && !a.employeeId ? `<label class="field"><span>Salário inicial (R$) *</span><input name="salarioInicial" type="number" min="0.01" step="0.01" required placeholder="Ex.: 2500.00"></label>` : ''}
""")
replace_once("""      if (a.stage !== ADMISSION_STAGES[idx]) {
        alert('A etapa mudou. Atualize a tela antes de avançar.');
        return false;
      }
      if (!Array.isArray(a.historicoEtapas)) a.historicoEtapas = [];
""", """      if (a.stage !== ADMISSION_STAGES[idx]) {
        alert('A etapa mudou. Atualize a tela antes de avançar.');
        return false;
      }
      const salarioInicial = Number(data.salarioInicial);
      if (proxima === 'Ativo' && !a.employeeId && (!Number.isFinite(salarioInicial) || salarioInicial <= 0 || !/^\\d+(?:\\.\\d{1,2})?$/.test(String(data.salarioInicial || '')))) {
        alert('Informe um salário inicial positivo, com no máximo duas casas decimais, para ativar o colaborador.');
        return false;
      }
      if (!Array.isArray(a.historicoEtapas)) a.historicoEtapas = [];
""")
replace_once("""DB.salaryHistory.push({ id: nextId('salaryHistory'), employeeId: empId, salario: 0, inicioVigencia: a.dataPrevista, fimVigencia: null, motivo: 'Admissão', cargo: a.cargo });""", """DB.salaryHistory.push({ id: nextId('salaryHistory'), employeeId: empId, salario: salarioInicial, inicioVigencia: a.dataPrevista, fimVigencia: null, motivo: 'Admissão', cargo: a.cargo });""")
replace_once("""    const registros = construirFruicoesDaForma(data.forma, data.inicio, data.inicio2, ciclo);
    if (stub) {
""", """    const registros = construirFruicoesDaForma(data.forma, data.inicio, data.inicio2, ciclo);
    // Reservas futuras e o segundo período pendente também ocupam dias do mesmo ciclo.
    // Ao preencher um stub automático ele é substituído, não somado duas vezes.
    const reservados = DB.vacations.filter(v => v.employeeId === e.id && v !== stub && v.statusFruicao !== 'Cancelado' && v.aquisitivoInicio === ciclo.aquisitivoInicio)
      .reduce((sum, v) => sum + (Number(v.diasGozo) || 0) + (Number(v.diasAbono) || 0), 0);
    const solicitados = registros.reduce((sum, v) => sum + (Number(v.diasGozo) || 0) + (Number(v.diasAbono) || 0), 0);
    if (reservados + solicitados > L.DIAS_DIREITO_FERIAS) {
      alert(`Este período aquisitivo já tem ${reservados} dia(s) reservados/usados. Restam ${Math.max(0, L.DIAS_DIREITO_FERIAS - reservados)} de ${L.DIAS_DIREITO_FERIAS}; esta programação solicita ${solicitados}. Confira os registros antes de continuar.`);
      return false;
    }
    if (stub) {
""")
replace_once("""      const employeeId = Number(data.employeeId);
      const dup = DB.payroll.find(p => p.employeeId === employeeId && p.competencia === data.competencia);
      if (dup) { alert('Já existe um lançamento de folha para este colaborador nesta competência (regra de integridade: 1 lançamento por colaborador/mês). Edite o existente em vez de duplicar.'); return; }
""", """      const employeeId = Number(data.employeeId);
      const competencia = String(data.competencia || '');
      if (!/^\\d{4}-(0[1-9]|1[0-2])-01$/.test(competencia)) {
        alert('Informe a competência no primeiro dia do mês (ex.: 2026-01-01).');
        return false;
      }
      // Detecta também registros antigos em dias diferentes do mesmo mês, sem alterar a base migrada.
      const dup = DB.payroll.find(p => Number(p.employeeId) === employeeId && String(p.competencia || '').slice(0, 7) === competencia.slice(0, 7));
      if (dup) { alert('Já existe um lançamento para este colaborador neste mês. Confira os registros de folha antes de continuar.'); return false; }
""")
replace_once("""<li><strong>Admissões</strong> — funil de pré-admissão com as etapas da diretriz, incluindo efetivação automática em colaborador CLT ao chegar em "Ativo".</li>""", """<li><strong>Admissões</strong> — funil de pré-admissão com as etapas da diretriz; a efetivação como CLT exige salário inicial positivo.</li>""")
replace_once("""<li><strong>TIP e matriz SST propositalmente vazios</strong>""", """<li><strong>Salvamento local</strong> — quando o navegador recusa a gravação, o sistema avisa e mantém os dados apenas na aba aberta para nova tentativa. Isso não substitui backup nem garante recuperação após fechar o navegador.</li>
        <li><strong>TIP e matriz SST propositalmente vazios</strong>""")
out.write_text(s, encoding='utf-8')
print(out, len(s), 'chars')
