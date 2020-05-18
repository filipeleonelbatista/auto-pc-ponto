<h1 align="center">
    <img alt="PCPONTO" title="#PCPONTO" src="img/logo.jpg" width="200px" />
</h1>

<h4 align="center">
  🚀 Automatização de ponto (PC Ponto)
</h4>

<p align="center">
  <a href="#tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

<br>

## Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)
- [Selenium for python](https://selenium-python.readthedocs.io/)
- [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## 💻 Projeto

O Projeto Automatização de ponto foi idealizado para pessoas que se esquecem de bater o ponto. Testado apenas com o app PC Ponto da Sigma
A idéia é rodar o app quando iniciar o seu pc, assim ele vai ler o arquivo horas.txt para ver as horas que deseja registrar o ponto. 
Quando chegar a hora ele irá mostrar um messagebox perguntando se deseja registrar o ponto, então abrirá o driver do Google Chrome 
(Necessário ter instalada a última versão) e irá ler o arquivo senhas.txt para colocar o usuario e senha do ponto. Em seguida
ele faz a verificação se o ponto foi registrado ou se houve algum erro. Caso der erro emitirá um messagebox com a informação do erro.

O projeto é simples mas auxiliou no aprendizado de automação de testes na web.


## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---

Feito com ♥ by Filipe Batista :wave: [Leonel Informática](https://leonelinformatica.com.br)
