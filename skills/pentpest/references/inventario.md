# Inventario completo

Las rutas siguientes son relativas al directorio de la skill. Leer únicamente lo pertinente. El código upstream está incluido sin instalar; sus configuraciones anidadas no se conectan automáticamente.

## Agentes (50)

- `assets/upstream/.claude/agents/auth-tester.md`
- `assets/upstream/.claude/agents/brain.md`
- `assets/upstream/.claude/agents/browser-agent.md`
- `assets/upstream/.claude/agents/browser-stealth-agent.md`
- `assets/upstream/.claude/agents/browser-verifier.md`
- `assets/upstream/.claude/agents/business-logic.md`
- `assets/upstream/.claude/agents/chain-builder.md`
- `assets/upstream/.claude/agents/cloud-recon.md`
- `assets/upstream/.claude/agents/config-auditor.md`
- `assets/upstream/.claude/agents/correlator.md`
- `assets/upstream/.claude/agents/cors-hunter.md`
- `assets/upstream/.claude/agents/csrf-hunter.md`
- `assets/upstream/.claude/agents/dast-devils-advocate.md`
- `assets/upstream/.claude/agents/file-upload.md`
- `assets/upstream/.claude/agents/graphql-audit.md`
- `assets/upstream/.claude/agents/idor-hunter.md`
- `assets/upstream/.claude/agents/info-disclosure.md`
- `assets/upstream/.claude/agents/js-analyzer.md`
- `assets/upstream/.claude/agents/llm-ai-hunter.md`
- `assets/upstream/.claude/agents/monitor.md`
- `assets/upstream/.claude/agents/nuclei-writer.md`
- `assets/upstream/.claude/agents/oauth-hunter.md`
- `assets/upstream/.claude/agents/open-redirect.md`
- `assets/upstream/.claude/agents/poc-builder.md`
- `assets/upstream/.claude/agents/privilege-escalation.md`
- `assets/upstream/.claude/agents/quality-check.md`
- `assets/upstream/.claude/agents/race-condition.md`
- `assets/upstream/.claude/agents/rce-hunter.md`
- `assets/upstream/.claude/agents/recon-ranker.md`
- `assets/upstream/.claude/agents/recon.md`
- `assets/upstream/.claude/agents/report-writer.md`
- `assets/upstream/.claude/agents/sast-danger-mapper.md`
- `assets/upstream/.claude/agents/sast-devils-advocate.md`
- `assets/upstream/.claude/agents/sast-entry-mapper.md`
- `assets/upstream/.claude/agents/sast-exploit-builder.md`
- `assets/upstream/.claude/agents/sast-file-ranker.md`
- `assets/upstream/.claude/agents/sast-flow-tracer.md`
- `assets/upstream/.claude/agents/sast-gap-analyzer.md`
- `assets/upstream/.claude/agents/sast-hunter.md`
- `assets/upstream/.claude/agents/scope-check.md`
- `assets/upstream/.claude/agents/sqli-hunter.md`
- `assets/upstream/.claude/agents/ssrf-hunter.md`
- `assets/upstream/.claude/agents/ssti-hunter.md`
- `assets/upstream/.claude/agents/subdomain-takeover.md`
- `assets/upstream/.claude/agents/validator.md`
- `assets/upstream/.claude/agents/vuln-scanner.md`
- `assets/upstream/.claude/agents/waf-profiler.md`
- `assets/upstream/.claude/agents/web3-auditor.md`
- `assets/upstream/.claude/agents/xss-hunter.md`
- `assets/upstream/.claude/agents/xxe-hunter.md`
## Comandos (26)

- `assets/upstream/.claude/skills/analyze/SKILL.md`
- `assets/upstream/.claude/skills/autopilot/SKILL.md`
- `assets/upstream/.claude/skills/brain/SKILL.md`
- `assets/upstream/.claude/skills/chain/SKILL.md`
- `assets/upstream/.claude/skills/correlate/SKILL.md`
- `assets/upstream/.claude/skills/cost/SKILL.md`
- `assets/upstream/.claude/skills/dupcheck/SKILL.md`
- `assets/upstream/.claude/skills/fullscan/SKILL.md`
- `assets/upstream/.claude/skills/hunt/SKILL.md`
- `assets/upstream/.claude/skills/learn/SKILL.md`
- `assets/upstream/.claude/skills/mindmap/SKILL.md`
- `assets/upstream/.claude/skills/monitor/SKILL.md`
- `assets/upstream/.claude/skills/new/SKILL.md`
- `assets/upstream/.claude/skills/pipeline/SKILL.md`
- `assets/upstream/.claude/skills/quality/SKILL.md`
- `assets/upstream/.claude/skills/quickscan/SKILL.md`
- `assets/upstream/.claude/skills/remember/SKILL.md`
- `assets/upstream/.claude/skills/report/SKILL.md`
- `assets/upstream/.claude/skills/resume/SKILL.md`
- `assets/upstream/.claude/skills/sast/SKILL.md`
- `assets/upstream/.claude/skills/status/SKILL.md`
- `assets/upstream/.claude/skills/submit/SKILL.md`
- `assets/upstream/.claude/skills/surface/SKILL.md`
- `assets/upstream/.claude/skills/sync/SKILL.md`
- `assets/upstream/.claude/skills/triage/SKILL.md`
- `assets/upstream/.claude/skills/validate/SKILL.md`
## Metodologías (13)

- `assets/upstream/skills/hunt-business-logic/SKILL.md`
- `assets/upstream/skills/hunt-idor/SKILL.md`
- `assets/upstream/skills/hunt-info-disclosure/SKILL.md`
- `assets/upstream/skills/hunt-llm-ai/SKILL.md`
- `assets/upstream/skills/hunt-oauth/SKILL.md`
- `assets/upstream/skills/hunt-rce/SKILL.md`
- `assets/upstream/skills/hunt-xss/SKILL.md`
- `assets/upstream/skills/hunting-methodology/SKILL.md`
- `assets/upstream/skills/recon-methodology/SKILL.md`
- `assets/upstream/skills/report-writing/SKILL.md`
- `assets/upstream/skills/sast-methodology/SKILL.md`
- `assets/upstream/skills/triage-validation/SKILL.md`
- `assets/upstream/skills/vuln-classes/SKILL.md`
## Utilidades CLI y auxiliares (25)

- `assets/upstream/tools/__init__.py`
- `assets/upstream/tools/autopilot_gate.py`
- `assets/upstream/tools/brain.py`
- `assets/upstream/tools/camofox_ctl.sh`
- `assets/upstream/tools/capture.py`
- `assets/upstream/tools/chain_plan.py`
- `assets/upstream/tools/chain_pressure_hook.py`
- `assets/upstream/tools/cost.py`
- `assets/upstream/tools/cost_hook.py`
- `assets/upstream/tools/coverage_record.py`
- `assets/upstream/tools/cvss_version_guard.py`
- `assets/upstream/tools/dedup_findings.py`
- `assets/upstream/tools/file_path_guard.py`
- `assets/upstream/tools/file_safety.py`
- `assets/upstream/tools/global_brain.py`
- `assets/upstream/tools/intel_engine.py`
- `assets/upstream/tools/journal.py`
- `assets/upstream/tools/pentest-statusline.sh`
- `assets/upstream/tools/response_tracker.py`
- `assets/upstream/tools/scaffold.py`
- `assets/upstream/tools/scope_check.py`
- `assets/upstream/tools/scope_hook.py`
- `assets/upstream/tools/statusline.py`
- `assets/upstream/tools/target_selector.py`
- `assets/upstream/tools/validity_guard.py`
## Reglas (9)

- `assets/upstream/rules/chain-table.md`
- `assets/upstream/rules/hunting.md`
- `assets/upstream/rules/identities.md`
- `assets/upstream/rules/mistakes.md`
- `assets/upstream/rules/never-submit.md`
- `assets/upstream/rules/payloads.md`
- `assets/upstream/rules/techniques.md`
- `assets/upstream/rules/vendor-status.md`
- `assets/upstream/rules/waf-bypass-protocol.md`
## MCP (15)

- `assets/upstream/mcp-bounty-server/models.py`
- `assets/upstream/mcp-bounty-server/providers/__init__.py`
- `assets/upstream/mcp-bounty-server/providers/base.py`
- `assets/upstream/mcp-bounty-server/providers/bugcrowd.py`
- `assets/upstream/mcp-bounty-server/providers/bugcrowd_auth.py`
- `assets/upstream/mcp-bounty-server/providers/extra.py`
- `assets/upstream/mcp-bounty-server/providers/hackerone.py`
- `assets/upstream/mcp-bounty-server/server.py`
- `assets/upstream/mcp-bounty-server/submissions.py`
- `assets/upstream/mcp-bounty-server/submit_handlers.py`
- `assets/upstream/mcp-bounty-server/tests/test_scope_serialization.py`
- `assets/upstream/mcp-bounty-server/tests/test_submit_handlers.py`
- `assets/upstream/mcp-bounty-server/tests/test_sync_program.py`
- `assets/upstream/mcp-writeup-server/server.py`
- `assets/upstream/mcp-writeup-server/tests/test_search_payloads.py`

## Resto de la suite

Consultar `assets/upstream/README.md` para los clientes soportados y requisitos; `providers/` contiene las traducciones, `hooks/` los hooks, `tests/` las pruebas originales, `wordlists/` las listas y `rag-builder/` el indexador opcional. Los binarios externos y el índice de writeups no están incluidos. Para uso local de los MCP consultar sus fuentes y requisitos antes de iniciar procesos. Nunca registrar rutas de este paquete como endpoints remotos.
