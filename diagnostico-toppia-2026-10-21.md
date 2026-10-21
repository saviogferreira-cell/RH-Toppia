# Diagnóstico funcional — Toppia com Feedbacks

Data: 21/10/2026. Arquivo testado: `toppia-com-feedbacks.html`. Esta é uma avaliação do protótipo local, não uma homologação para produção.

## Como testei

Executei 12 verificações automatizadas em cópia isolada dos dados embutidos no HTML, carregando os scripts em um ambiente JavaScript simulado. Cobri renderização das rotas principais, acesso de gestor, avaliação por competências, validação da escala de 1 a 5, duas avaliações e cálculo de evolução, escape de texto, conclusão de ação, gravação e recarga simuladas, folha, admissão, férias, erro de armazenamento e restauração. Os 12 testes atingiram os comportamentos esperados pelo roteiro; quatro deles **reproduziram defeitos** e um reproduziu um risco de perda silenciosa. O dashboard foi visto na prévia, mas não houve automação de cliques em um Chrome real. Não testei a extração de PDFs com arquivos reais nem conferi cálculos trabalhistas com a contabilidade.

## O que funciona no escopo testado

A aplicação carrega a base incorporada e renderiza as rotas principais sem erro de execução no ambiente simulado. A nova aba Feedbacks registra avaliações, rejeita nota fora de 1–5, calcula a média e a diferença entre avaliações, mostra o histórico, conclui planos de ação e recupera o registro após a recarga simulada com armazenamento disponível. O texto livre da avaliação é escapado na visualização. A visão de feedback do perfil Gestor filtra colaboradores fora da equipe selecionada, mas o seletor de perfil não é autenticação.

## Achados reproduzidos

**Alta — Folha permite lançamentos para o mesmo mês.** O campo “Competência (1º dia do mês)” aceita 03/01/2026 mesmo quando existe 01/01/2026 para o mesmo colaborador, pois a verificação de duplicidade compara datas completas, não mês/ano (`toppia-com-feedbacks.html`, linhas 2585–2600). O resultado foram dois lançamentos para janeiro. Corrigir com normalização para o primeiro dia e validação de unicidade por colaborador e mês; conferir duplicidades já existentes antes de usar os totais.

**Alta — Admissão ativa colaborador com salário zero.** Ao avançar uma pré-admissão até “Ativo”, o código cria a vigência salarial com valor 0 sem solicitar o salário (`linhas 2327–2373`). Reproduzi o fluxo até a ativação. Exigir remuneração inicial válida ou deixar a ficha pendente antes da inclusão em folha e indicadores.

**Média/alta — Férias excedem os dias de um período aquisitivo.** Registrei duas reservas de 30 dias para a mesma pessoa e o mesmo período; ambas foram aceitas (`linhas 2052–2073`). Impedir a gravação quando a soma de períodos confirmados e reservados ultrapassar o direito disponível, com tratamento explícito de abono e pendências.

**Média — Duplicidade na folha fecha o formulário sem salvar.** Quando a competência exata já existe, a ação exibe um alerta e retorna `undefined`; o modal interpreta isso como sucesso e fecha (`linhas 1955–2003 e 2595–2599`). Retornar `false` para manter o formulário aberto e orientar a correção. A mensagem sugere editar o lançamento existente, mas não identifiquei ação de edição nessa tela.

**Alta — Erro ao salvar é ocultado.** Simulei uma falha de `localStorage.setItem`; `saveDB()` ignorou a exceção e prosseguiu sem avisar (`linhas 2779–2781`). O usuário pode acreditar que o feedback ou outro registro foi salvo quando não foi. Mostrar falha de gravação, preservar o formulário e fornecer exportação/backup.

## Limitações importantes

O HTML contém dados pessoais da base e depende do armazenamento local do navegador; não há servidor, sincronização entre usuários, backup automático ou autenticação segura. Os perfis são escolhidos no próprio menu, de modo que a filtragem de “Gestor” é uma conveniência de interface, não proteção de acesso. Restaurar a base apaga também os feedbacks locais. Evite usar este arquivo como sistema oficial de RH ou compartilhá-lo indiscriminadamente. Antes de produção, separar dados do HTML, adotar backend e autenticação com permissões verificadas no servidor, política de retenção e backups, e validar regras de folha/férias com RH e DP.

## Prioridade sugerida

Primeiro, proteger dados e impedir perdas silenciosas. Em seguida, corrigir unicidade da folha, remuneração na admissão e saldo de férias. Depois, executar testes de ponta a ponta no Chrome com uma base de homologação e casos reais de importação PDF. Os achados adicionais apontados por leitura de código (por exemplo, associação de duplicatas em importação de ponto) ainda exigem reprodução e não entram como falhas confirmadas neste diagnóstico.
