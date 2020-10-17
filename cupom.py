# coding: utf-8

class Endereco:
  
  def __init__(self, logradouro, numero, complemento, bairro, municipio, 
      estado, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep

  def validar_campos_obrigatorios(self):
    
    if not self.logradouro:
      raise Exception ("O campo logradouro do endereço é obrigatório")

    if not self.municipio:
      raise Exception ("O campo município do endereço é obrigatório")

    if not self.estado:
      raise Exception ("O campo estado do endereço é obrigatório")

  def dados_endereco(self):

    self.validar_campos_obrigatorios()

    _logradouro = self.logradouro + ", "
    _numero = self.numero and str(self.numero) or "s/n"
    _complemento = self.complemento and " " + self.complemento or ""
    _bairro = self.bairro and self.bairro + " - " or ""
    _municipio = self.municipio + " - "

    _cep = self.cep and ("CEP:" + self.cep) or ""

    return (f"""{_logradouro}{_numero}{_complemento}
{_bairro}{_municipio}{self.estado}
{_cep}""")

class Loja:
  
  def __init__(self, nome_loja, endereco, telefone, observacao, cnpj, 
      inscricao_estadual):
    self.nome_loja = nome_loja
    self.endereco = endereco
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

  def validar_campos_obrigatorios(self):

    if not self.nome_loja:
      raise Exception ("O campo nome da loja é obrigatório")

    if not self.cnpj:
      raise Exception ("O campo CNPJ da loja é obrigatório")

    if not self.inscricao_estadual:
      raise Exception ("O campo inscrição estadual da loja é obrigatório")

  def dados_loja(self):

    self.validar_campos_obrigatorios()

    _telefone = self.telefone and ("Tel " + self.telefone) or ""
    _telefone = (_telefone and self.endereco.cep) and (" " + _telefone) or _telefone

    _observacao = self.observacao and self.observacao or ""

    _cnpj = "CNPJ: " + self.cnpj
    _inscricao_estadual = "IE: " + self.inscricao_estadual
    
    return (f"""{self.nome_loja}
{self.endereco.dados_endereco()}{_telefone}
{_observacao}
{_cnpj}
{_inscricao_estadual}""")

class Venda:

  def __init__(self, loja, datahora, ccf, coo):
    self.loja = loja
    self.datahora = datahora
    self.ccf = ccf
    self.coo = coo

  def validar_campos_obrigatorios(self):

    if not self.loja:
      raise Exception ("O campo loda da venda é obrigatório")
       
    if not self.datahora:
      raise Exception ("O campo datahora da venda é obrigatório")

    if not self.ccf:
      raise Exception ("O campo ccf da venda é obrigatório")

    if not self.coo:
      raise Exception ("O campo coo da venda é obrigatório")

  def dados_venda(self):

    self.validar_campos_obrigatorios()

    texto_data = self.datahora.strftime("%d/%m/%Y")
    texto_hora = self.datahora.time().strftime("%H:%M:%S")
    
    _hora = texto_hora +"V"
    _ccf = "CCF:" + self.ccf
    _coo = "COO: " + self.coo
    
    return (f"""{texto_data} {_hora} {_ccf} {_coo}""")

  def imprime_cupom(self):
    dados_loja = self.loja.dados_loja()
    dados_venda = self.dados_venda()
    return '''{loja}
------------------------------
{venda}'''.format(loja=dados_loja, venda=dados_venda)
                                                          
