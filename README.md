# 🛡️ Análise de Vulnerabilidades em Arquitetura de Rede (UC Segurança em Redes e Computadores)

## Visão Geral do Projeto

Este repositório documenta um projeto de análise de segurança focado na identificação e mitigação de vulnerabilidades numa arquitetura de rede de média dimensão. O objetivo foi aplicar os princípios de Confidencialidade, Integridade e Disponibilidade (CIA) para reforçar a postura de segurança do sistema.

[cite_start]O trabalho foi desenvolvido no âmbito da Unidade Curricular de **Segurança em Redes e Computadores (21181)** da Licenciatura em Engenharia Informática[cite: 4, 9].

## 🗺️ Conteúdo do Repositório

* **`./enunciado/`**: Imagem do esquema de rede e descrição do problema original (autorizado pelo docente).
* **`./relatorio/`**: Relatório de análise e proposta de mitigação em formato PDF.
* **`./scripts_e_dados/`**: Scripts Python utilizados para a demonstração criptográfica.

## 🔑 Metodologia de Análise e Modelação de Ameaças

A análise seguiu uma abordagem estruturada, identificando pontos críticos de falha, modelando possíveis caminhos de ataque e propondo controlos de segurança por camadas (Defesa em Profundidade).

### 1. Vulnerabilidades Críticas Identificadas

[cite_start]Foram identificadas cinco vulnerabilidades arquitetónicas que aumentavam significativamente o risco de comprometimento da rede[cite: 29, 214]:

1.  [cite_start]**Falta de Segmentação WLAN/LAN:** Permitia o movimento lateral de ataques devido à ausência de *firewall* interna e VLANs[cite: 30, 31, 107].
2.  [cite_start]**Posicionamento Incorreto do IDS/IPS:** O sistema de deteção/prevenção de intrusões estava em modo paralelo, falhando em monitorizar o tráfego de entrada e permitir a passagem de tráfego malicioso[cite: 35, 36, 37].
3.  [cite_start]**Exposição do Database Server:** O servidor com dados sensíveis estava incorretamente posicionado na DMZ, violando o princípio da Defesa em Profundidade[cite: 38, 39, 40].
4.  [cite_start]**Exposição de Servidores Públicos:** O WebServer e o Email Server estavam vulneráveis devido ao mau posicionamento do IDS/IPS[cite: 43, 44].
5.  [cite_start]**Firewall Única:** Criação de um ponto único de falha no perímetro da rede[cite: 45, 47].

### 2. Exemplos de Modelação de Ataque (Attack Trees)

[cite_start]Foram desenvolvidos diagramas de Árvores de Ataque, demonstrando vetores de exploração para objetivos específicos[cite: 51, 74]:

| Objetivo | Vetores de Ataque | Ameaças Chave |
| :--- | :--- | :--- |
| [cite_start]**Roubo de Dados** (Database Server na DMZ) [cite: 60] | [cite_start]SQL Injection, Phishing para obter credenciais, Brute-force SSH [cite: 55, 56, 65, 66] | [cite_start]Roubo de informação sensível, Destruição de dados [cite: 50] |
| [cite_start]**Controlar Rede Interna** (Execução de Ransomware) [cite: 83] | [cite_start]Comprometimento do dispositivo móvel via Phishing ou Man-in-the-Middle (Wi-Fi), seguido de **Movimento Lateral** da WLAN para a LAN [cite: 75, 77, 79, 81] | [cite_start]Infeção por ransomware, Sniffing [cite: 50] |

## 💡 Soluções e Controlos de Segurança Propostos

[cite_start]A estratégia de mitigação focou-se na implementação de controlos ativos e passivos, transformando a rede numa infraestrutura defensável[cite: 219, 233].

| Controlo Proposto | Ação de Mitigação | Princípios Reforçados |
| :--- | :--- | :--- |
| **Segmentação e Isolamento** | [cite_start]Criação de **VLANs** e implementação de uma **Firewall Interna** com regras ACL para isolar a WLAN da LAN[cite: 112, 113, 215]. | [cite_start]Confidencialidade e Integridade [cite: 119] |
| **Monitorização do Perímetro** | [cite_start]Reposicionamento do IDS/IPS em modo **in-line** e instalação de um **WAF (Web Application Firewall)**[cite: 125, 126, 216, 217]. | [cite_start]Confidencialidade e Integridade [cite: 129] |
| **Autenticação Forte** | [cite_start]Implementação de **MFA (Autenticação Multifator)** para acessos administrativos e VPN[cite: 136, 227]. | [cite_start]Confidencialidade [cite: 140] |
| **Redundância/DRP** | [cite_start]Implementação de **UPS** para servidores críticos e Plano de Contingência (DRP) com backups off-site[cite: 137, 150, 153]. | [cite_start]Disponibilidade [cite: 143] |

## 🔐 Demonstração Criptográfica Híbrida

[cite_start]Como parte da solução, foi demonstrada a importância e a implementação de uma solução criptográfica híbrida (`AES+RSA`) em Python, que garante a confidencialidade e integridade das comunicações[cite: 222].

* [cite_start]**AES (Simétrico):** Usado para a encriptação/decifração rápida de volumes de dados[cite: 158, 168].
* [cite_start]**RSA (Assimétrico):** Usado para a troca segura da chave de sessão AES, resolvendo o problema de gestão de chaves da encriptação simétrica[cite: 175, 193, 195].

[cite_start]O código de demonstração deste esquema híbrido pode ser encontrado na secção `./scripts_e_dados/`[cite: 196].

## 📚 Tecnologias Chave / Referências

* **Ferramentas Lógicas:** Modelação de Ameaças (Threat Modeling), Princípios CIA, Defesa em Profundidade.
* [cite_start]**Implementação:** Python, Biblioteca `cryptography.hazmat.primitives` (AES-GCM e RSA-OAEP)[cite: 160, 178, 252].
* [cite_start]**Referências Académicas:** Stallings, W. (Computer Security), OWASP Foundation, NCSC (Attack Trees)[cite: 239, 240, 243].
