# Typografi og talformat

Load when the pre-emit scanner in SKILL.md flags typography, numbers, dates, currency, or comma system. MT Danish keeps English conventions; these are mechanical and the model gets them wrong constantly.

| Element | Forkert | Rigtigt |
| --- | --- | --- |
| Tankestreg | `15. maj—og derefter` | `15. maj – og derefter` (halvlang streg, mellemrum om) |
| Decimaltal | `1.1 mia.`, `9.8` | `1,1 mia.`, `9,8` |
| Tusindtal | `1,000,000` | `1.000.000` |
| Dato i brødtekst | `May 15` | `15. maj`. Numeric `15/5/2026` is also correct Danish; `15. maj 2026` is often clearer in running text. For ambiguous dates such as `03/04/2026`, preserve the form and ask which source locale applies. |
| Store tal | `$100 billion` | `100 milliarder $`. Engelsk *billion* = dansk *milliard*. Bevar valutabetegnelsen. |
| Valuta i brødtekst | `DKK 100`; `$5` | `100 DKK`; `5 $` eller `5 dollar`. Brug kun `kr.` når konteksten allerede fastslår danske kroner. I tabeller kan valutaen stå foran beløbet. |
| Procent | `20 %` og senere `30%` i samme tekst | `20 %` og `30 %`, eller `20%` og `30%`. Mellemrum er Dansk Sprognævns anbefaling; formen uden er også udbredt. Vælg én form og hold den. |
| Procent i sammensætninger | `20 %-rabat`, `43 %-tallet` | `20-%-rabat`, `43-%-tallet` |
| Klokkeslæt | `3:00 PM` | `kl. 15` eller `kl. 15.00` |
| Forkortelser | `e.g.`, `i.e.` | `fx`, `dvs.`. Både `etc.` og `osv.` er korrekte på dansk. |
| Komma ved ledsætninger | `Vi anbefaler, at I patcher når fejlen er rettet` (blandede systemer) | `Vi anbefaler, at I patcher, når fejlen er rettet` eller `Vi anbefaler at I patcher når fejlen er rettet`. Slutkomma sættes normalt i begge systemer; der findes snævre undtagelser. Startkomma ved almindelige ledsætninger er valgfrit, men selvstændige og parentetiske ledsætninger har fast komma. Vælg ét system og hold det. |
| Ugedage og måneder | `Mandag`, `Maj` | `mandag`, `maj` (småt på dansk) |
| Nationalitetsadjektiver | `Dansk lovgivning` | `dansk lovgivning` (`Danmark` stort, `dansk` småt) |
| Overskrifter | `Strategiske Partnerskaber Og Vækst` | `Strategiske partnerskaber og vækst` |
| Anførselstegn i ubeskyttet prosa | blanding af `"..."`, `“...”` og `»...«` | Alle tre former kan bruges. Vælg én og hold den. Do not normalize attributed quotes, mandated wording, code or paste-ready strings. |
