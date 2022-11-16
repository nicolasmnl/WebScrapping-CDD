import scrapy
from .utils import get_links_deputadas, build_csv, get_csv_header, get_nome, get_info_plenario_comissao, get_data_nascimento, get_gastos_par_gab, get_salario_bruto, get_qtd_viagens
import csv


info_deputada = []
class DeputadasSpider(scrapy.Spider):
    name = "spider_gwen"
    def start_requests(self):
        
        urls = get_links_deputadas()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'deputada.html'
        
        # Retorna o nome da deputada
        nome = get_nome(response)
        print(nome)
        genero = 'F'
        # Retorna todas as informações de plenario e comissao (presenca, ausencia, etc)
        info_plen_com = get_info_plenario_comissao(response)

        # Retorna a data de nascimento da deputada

        data_nascimento = get_data_nascimento(response)

        gastos_par_gab = get_gastos_par_gab(response)

        salario = get_salario_bruto(response)
        
        qtd_viagens = get_qtd_viagens(response)

        info_deputada.append(build_csv(nome, genero, data_nascimento, info_plen_com, gastos_par_gab, salario, qtd_viagens))
        
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        
        header = get_csv_header()
        with open('info_deputadas.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        
            writer.writerows(info_deputada)
        
