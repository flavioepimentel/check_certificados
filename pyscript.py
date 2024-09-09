import os
import re
from datetime import datetime
import shutil
import pytz

# Defina os caminhos dos diretórios
valid_dir = '//serv-dados/SETOR SUPORTE/CERTIFICADOS/1. CERTIFICADOS ATIVOS'
expired_dir = '//serv-dados/SETOR SUPORTE/CERTIFICADOS/2. CERTIFICADOS VENCIDOS'

# Padrão regex para encontrar a data no formato " dd-MM-yyyy"
date_pattern = re.compile(r'\s\d{2}-\d{2}-\d{4}')

# Função para verificar e mover arquivos


def process_files():
    # Iterar sobre todos os arquivos no diretório 'Validos'
    for filename in os.listdir(valid_dir):
        file_path = os.path.join(valid_dir, filename)

        # Verificar se é um arquivo
        if os.path.isfile(file_path):
            # Verificar se o nome do arquivo contém o padrão de data
            match = date_pattern.search(filename)

            if match:
                # Extrair a data do nome do arquivo
                date_str = match.group().strip()
                file_date = datetime.strptime(date_str, '%d-%m-%Y')

                # Verificar se a data é menor que a data atual
                if file_date < datetime.now():
                    # Mover o arquivo para o diretório 'Vencidos'
                    shutil.move(file_path, os.path.join(expired_dir, filename))
                    print(f'{filename} movido para Vencidos')
                    with open("log_vencidos.txt", "w") as file:
                        file.write(f'{filename} movido para Vencidos ---> {datetime.strftime(datetime.now(tz=pytz.timezone('America/Bahia')), "%Y-%m-%d %H:%M:%S.%f")}')
                else:
                    print(f'{filename} ainda é válido')
            else:
                print(f'{filename} não contém uma data válida')
                with open("log_data_invalidas.txt", "w") as file:
                    file.write(f'{str(filename)} não contém uma data válida ---> {datetime.strftime(datetime.now(tz=pytz.timezone('America/Bahia')), "%Y-%m-%d %H:%M:%S.%f")}')
        else:
            print(f'{filename} não é um arquivo')
            with open("log_arquivos_invalidos.txt", "w") as file:
                file.write(f'{filename} não é um arquivo ---> {datetime.strftime(datetime.now(tz=pytz.timezone('America/Bahia')), "%Y-%m-%d %H:%M:%S.%f")}')


if __name__ == '__main__':
    process_files()
