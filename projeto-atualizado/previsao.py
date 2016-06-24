from xml.etree import ElementTree
from urllib.request import urlopen

class PrevisaoTempo:
    
    TEMPO = {'ec':'Encoberto com Chuvas Isoladas',
             'ci':'Chuvas Isoladas',
             'c':'Chuva',
             'in':'Instável',
             'pp':'Possibilidade de Pancadas de Chuva',
             'cm':'Chuva pela Manhã',
             'cn':'Chuva à Noite',
             'pt':'Pancadas de Chuva à Tarde',
             'pm':'Pancadas de Chuva pela Manhã',
             'np':'Nublado e Pancadas de Chuva',
             'pc':'Pancadas de Chuva',
             'pn':'Parcialmente Nublado',
             'cv':'Chuvisco',
             'ch':'Chuvoso',
             't':'Tempestade',
             'ps':'Predomínio de Sol',
             'e':'Encoberto',
             'n':'Nublado',
             'cl':'Céu Claro',
             'nv':'Nevoeiro',
             'g':'Geada',
             'ne':'Neve',
             'nd':'Não Definido',
             'pnt':'Pancadas de Chuva à Noite',
             'psc':'Possibilidade de Chuva',
             'pcm':'Possibilidade de Chuva pela Manhã',
             'pct':'Possibilidade de Chuva à Tarde',
             'pcn':'Possibilidade de Chuva à Noite',
             'npt':'Nublado com Pancadas à Tarde',
             'npn':'Nublado com Pancadas à Noite',
             'ncn':'Nublado com Possibilidade de Chuva à Noite',
             'nct':'Nublado com Possibilidade de Chuva à Tarde',
             'ncm':'Nublado com Possibilidade de Chuva pela Manhã',
             'npm':'Nublado com Pancadas de Chuva pela Manhã',
             'npp':'Nublado com Possibilidade de Chuva',
             'vn':'Variação de Nebulosidade',
             'ct':'Chuva à Tarde',
             'ppn':'Possibilidade de Pancadas de Chuva à Noite',
             'ppt':'Possibilidade de Pancadas de Chuva à Tarde',
             'ppm':'Possibilidade de Pancadas de Chuva pela Manhã'}


    data_url = ""

    def __init__(self, cid):
        self.data_url = "http://servicos.cptec.inpe.br/XML/cidade/" + str(cid) + "/previsao.xml"

    def situacao(self, abr):    
        return self.TEMPO[abr]
    
    def pesquisar(self):
        tempos = {}
        
        with urlopen(self.data_url) as datafile:
            data = ElementTree.parse(datafile)#converte para um ElementTree
            root = data.getroot()#recupera o root do arquivo xml (root é a tag raiz -> <collection> no nosso caso)
            tagPrev = root.findall("previsao")[0]
            for j in range(len(tagPrev.getchildren())):
               tempos[tagPrev[j].tag] = tagPrev[j].text
                
        return tempos
    
#p = PrevisaoTempo(243)
#p.pesquisar()
#print(p.pesquisar())


