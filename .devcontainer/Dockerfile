# Imagem base do Container principal:
    FROM mcr.microsoft.com/devcontainers/anaconda

# Copiar o arquivo com as configurações do Anaconda para dentro do Container:
    COPY environment.yml .

# Copiar scripts de instalação/configuração:
    COPY scripts/configConda.sh .

# Conceder permissão de execução para os scripts de instalação/configuração:
    RUN chmod +x ./configConda.sh

# Rodar os scripts:
    RUN ./configConda.sh
