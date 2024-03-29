from bs4 import BeautifulSoup
import yaml

html = '''    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Cicloviário do Município de São Paulo.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Cicloviário do Município de São Paulo</h2>
                  <p class="card__snippet">O Plano Cicloviário visa definir a rede cicloviária da cidade e seus elementos de apoio, orientado para a estruturação de um sistema integrado. Visa promover a intermodalidade e a conexão com os principais equipamentos de transportes públicos, garantir a segurança do uso da bicicleta na malha viária da cidade e promover ações que incentivem o uso do modal de modo a expandi-lo e consolidá-lo na estrutura viária.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PlanClima.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Ação Climática de São Paulo</h2>
                  <p class="card__snippet">O PlanClima SP é o instrumento voltado à orientação do planejamento e gestão das políticas setoriais da Administração Municipal Direta e Indireta, visando estimular a redução das emissões de gases de efeito estufa e a adaptação aos impactos da mudança do clima, bem como transformar os atuais modos de produção e de consumo no âmbito do Município de São Paulo.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano de Ação do Plano Municipal pela Primeira Infância.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Ação do Plano Municipal pela Primeira Infância</h2>
                  <p class="card__snippet">O Plano Municipal pela Primeira Infância de São Paulo (PMPI), estabelecido em 2018, requer a elaboração de um plano de ação quadrienal alinhado aos seus princípios e diretrizes. O Plano de Ação 2021-2024 foi desenvolvido com a participação de 15 secretarias municipais, baseado nos quatro eixos estratégicos, 31 metas e 135 estratégias do PMPI. Foram definidas diretrizes estratégicas, incluindo a redução das desigualdades, com foco nas questões raciais, e o enfrentamento dos impactos da pandemia de Covid-19, para orientar as iniciativas nos próximos quatro anos.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano de Ação Agenda 2030.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Ação para Implementação da Agenda 2030</h2>
                  <p class="card__snippet">A Agenda 2030 é um compromisso global com o desenvolvimento sustentável, adotado em 2015 por 193 países membros da ONU, incluindo o Brasil. Ela amplia e reafirma os compromissos estabelecidos em 2000 pelos Objetivos do Milênio (ODM) e visa a promover políticas para erradicar a pobreza, a fome, melhorar o acesso a serviços básicos e enfrentar desafios socioambientais. Fundamentada em cinco princípios (Pessoa, Planeta, Paz, Prosperidade e Parcerias), a Agenda 2030 inclui 17 Objetivos de Desenvolvimento Sustentável (ODS) e 169 metas correspondentes.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano de Ações do Plano Diretor de Drenagem.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Ações do Plano Diretor de Drenagem</h2>
                  <p class="card__snippet">O Plano de Ações tem como principal objetivo cumprir a função de ferramenta para a programação e elaboração de um cronograma de obras para o controle de cheias, além de fornecer suporte à decisão de priorizar determinada intervenção em detrimento das demais, no sistema de macrodrenagem propostas nos cadernos de Bacia Hidrográfica e no Plano Diretor de Drenagem da Bacia do Alto Tietê – PDMAT.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano de Desenvovimento do Polo de Ecoturismo de São Paulo.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Desenvolvimento do Turismo Sustentável (Polo de Ecoturismo de São Paulo)</h2>
                  <p class="card__snippet">O Polo de Ecoturismo, localizado no extremo sul de São Paulo, foi oficialmente criado em 2014 e abrange mais de 400 quilômetros quadrados, correspondendo a cerca de 28% da área total da cidade. Dividido em três distritos, Marsilac, Parelheiros e parte do Grajaú, incluindo o bairro Ilha do Bororé, a região destaca-se por suas belezas naturais, como a mata atlântica preservada, unidades de conservação, rios e cachoeiras. No entanto, o desenvolvimento desordenado contribuiu para problemas sociais e urbanísticos, como ocupações desordenadas e desmatamento. A Prefeitura de São Paulo, por meio da SPTuris, optou por um plano de desenvolvimento turístico exclusivo para o Polo de Ecoturismo, visando orientar estrategicamente a atuação dos envolvidos no turismo, sejam do setor público, privado ou terceiro setor.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PGIRS.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Gestão Integrada de Resíduos Sólidos da Cidade de São Paulo</h2>
                  <p class="card__snippet">O Plano de Gestão Integrada de Resíduos Sólidos (PGIRS)  é um dos mais importantes instrumentos da Política Nacional de Resíduos Sólidos. Estabelece, para todos os atores envolvidos com os resíduos sólidos (produtores de mercadorias que geram resíduos nas fases de produção, consumo e pós-consumo, comerciantes, distribuidores, importadores, prestadores de serviço público ou privado de manejo de resíduos sólidos e consumidores), a partir da situação atual da gestão dos resíduos sólidos, como se pretende atuar para atingir, em determinado período temporal, os objetivos da Política. A diretriz fundamental que norteia o Plano é a observação da seguinte ordem de prioridade: não geração, redução, reutilização, reciclagem, tratamento dos resíduos sólidos e disposição final ambientalmente adequada apenas dos rejeitos.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano de Segurança Viária do Municipio.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano de Segurança Viária do Município</h2>
                  <p class="card__snippet">O Plano de Segurança Viária é um instrumento fundamental para orientar as políticas públicas de segurança viária do Município. Ele é uma peça de planejamento que visa coordenar e unificar as ações da Prefeitura com o objetivo de reduzir o número de fatalidades nas vias urbanas. Este plano está alinhado com iniciativas globais, como a Década de Ação para Segurança Global no Trânsito da ONU e a Agenda 2030 de Desenvolvimento Sustentável, que inclui a meta de garantir sistemas de transporte seguros, acessíveis e sustentáveis para todos. No contexto nacional, o plano se baseia na Lei Federal nº 13.614/18, que estabelece o Plano Nacional de Redução de Mortes e Lesões no Trânsito. Este plano tem como objetivo reduzir pela metade o número de mortes por grupo de veículos e por grupos de habitantes até 2028.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PDMASsp.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Decenal de Assistência Social da Cidade de São Paulo</h2>
                  <p class="card__snippet">O PDMASsp busca identificar elementos que possam ajudar a compreender a realidade e os indicadores de vulnerabilidade social da população que vive em determinadas áreas, fazendo uma abordagem do território a partir de suas complexidades. O texto evita deliberadamente o termo "território", muitas vezes utilizado de forma equivocada, compreendido apenas como um espaço geográfico no mapa. Aborda, em contrapartida, o território a partir da perspectiva de Milton Santos, ou seja, de que o território é um construto histórico que envolve uma complexa rede de forças, culturas e relações. É, em suma, uma força em constante movimento, que exige uma compreensão mais profunda e holística de sua abordagem.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Decenal Municipal de Atendimento Socioeducativo.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Decenal de Atendimento Socioeducativo</h2>
                  <p class="card__snippet">O Plano Decenal de Atendimento Socioeducativo do Município de São Paulo segue as diretrizes estabelecidas pelo Sistema Nacional de Atendimento Socioeducativo (SINASE), conforme a Lei nº 12.594 de 2012. Em colaboração com o Conselho Nacional dos Direitos da Criança e do Adolescente (CONANDA) e a Secretaria Especial de Direitos Humanos da Presidência da República, foi promovido um processo de debate e mobilização para elaborar planos de atendimento socioeducativo em níveis nacional, estadual e municipal, de forma articulada, o que, no que se refere ao município, resultou no Plano Decenal de Atendimento Socioeducativo que tem como objetivo organizar a execução das medidas socioeducativas, priorizando a garantia dos direitos fundamentais dos adolescentes que cumprem essas medidas em meio aberto.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PDE.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Diretor Estratégico</h2>
                  <p class="card__snippet">O Plano Diretor Estratégico do Município de São Paulo é uma lei municipal que orienta o desenvolvimento e o crescimento da cidade até 2030. Elaborado com a participação da sociedade, o PDE direciona as ações dos produtores do espaço urbano, públicos ou privados, para que o desenvolvimento da cidade seja feito de forma planejada e atenda às necessidades coletivas de toda a população, visando garantir uma cidade mais moderna, equilibrada, inclusiva, ambientalmente responsável, produtiva e, sobretudo, com qualidade de vida.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PETIC.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Estratégico de Tecnologia da Informação e Comunicação</h2>
                  <p class="card__snippet">A inovação e a tecnologia frequentemente são associadas à disrupção e ao desenvolvimento de produtos digitais, porém, isso só é viável com uma política pública focada no desenvolvimento das pessoas, capacitando-as continuamente. O PETIC, resultado do trabalho dos servidores da prefeitura, visa capacitar tanto os agentes públicos quanto os cidadãos no uso da tecnologia, visando otimizar serviços e promover inclusão social. O plano define metas estratégicas para a Administração Municipal e temas de tecnologia a serem desenvolvidos, alinhando-se com outros planejamentos setoriais, como o Plano de Metas, para suportar as políticas públicas municipais.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Intersetorial de Políticas Públicas para o Envelhecimento.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Intersetorial de Políticas Públicas para o Envelhecimento</h2>
                  <p class="card__snippet">O Plano Intersetorial de Políticas Públicas (2021-2024) é um instrumento crucial de gestão pública que resultou de discussões entre técnicos de quinze secretarias municipais e representantes do Conselho Municipal do Idoso. Seu objetivo é definir metas e ações para promover o envelhecimento populacional de maneira condigna aos direitos humanos. Baseado em diversas perspectivas, será uma referência para o planejamento e a melhoria dos programas e serviços destinados aos idosos em São Paulo. Construído a partir de demandas da sociedade civil, o plano reflete os quatro eixos do Envelhecimento Ativo e Saudável, definidos pela Organização Mundial da Saúde, visando melhorar a qualidade de vida à medida que as pessoas envelhecem.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - IncluiSampa.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Ações para Pessoas com Deficiência</h2>
                  <p class="card__snippet">O Inclui Sampa, Plano Municipal de Ações para Pessoas com Deficiência, nasceu do diálogo transversal e intersecretarial entre a Secretaria Municipal da Pessoa com Deficiência (SMPED) e a Cidade de São Paulo, a fim de apresentar compromissos e metas para aperfeiçoar a qualidade, ampliar a quantidade e aumentar o número de serviços ofertados às pessoas com deficiência no município, de forma a pactuar e promover ações articuladas com diferentes órgãos municipais, bem como estabelecer metas e indicadores que permitam acompanhar a execução do plano e efetuar eventuais correções, em um processo de melhoria contínua.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PlanClima2.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Agroecologia e Desenvolvimento Rural Sustentável e Solidário</h2>
                  <p class="card__snippet">O Plano Municipal de Agroecologia e Desenvolvimento Rural Sustentável, elaborado em conjunto com o Conselho Municipal de Desenvolvimento Rural Solidário e Sustentável (CMDRSS), é resultado de oficinas temáticas realizadas com agricultores e movimentos sociais em 2018, seguidas por uma consulta pública. O plano visa promover a inclusão econômica e incentivar o crescimento das atividades agroecológicas no município, melhorando as condições de trabalho dos agricultores familiares urbanos e rurais.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PMAU.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Arborização Urbana</h2>
                  <p class="card__snippet">O Plano Municipal de Arborização Urbana (PMAU) é um instrumento para o planejamento e gestão da arborização em São Paulo, visando aumentar a resiliência da cidade às mudanças climáticas, qualificar a paisagem e satisfazer a população, com base nos princípios da ecologia e das cidades inteligentes. O PMAU é fundamentado em ações participativas e contribui para a implementação dos Objetivos de Desenvolvimento Sustentável (ODS), especialmente os relacionados às cidades sustentáveis, ação climática e vida terrestre. Elaborado por um grupo técnico e com participação da população, o plano consiste em sete capítulos que abordam temas como conhecimento, engajamento, plantio, cuidado e integração. Um diagnóstico amplo da arborização municipal embasa um plano de ação com objetivos específicos, como ampliar e qualificar a cobertura arbórea, envolver a comunidade, basear as ações em evidências científicas e promover a integração institucional para uma gestão eficaz da arborização.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Planpavel.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Áreas Protegidas Áreas Verdes e Espaços Livres</h2>
                  <p class="card__snippet">O Plano Municipal de Áreas Protegidas, Áreas Verdes e Espaços Livres (PLANPAVEL), aprovado pela Resolução CADES 228/CADES/2022, é um instrumento de planejamento e gestão que tem como objetivo principal definir uma política para a gestão e provisão de áreas verdes e proteção do patrimônio ambiental no município de São Paulo. O PLANPAVEL segue os princípios do Plano Diretor Estratégico do município e de documentos de organismos nacionais e internacionais relacionados ao meio ambiente urbano. Além disso, está alinhado com a Nova Agenda Urbana, que propõe cidades inclusivas, seguras, saudáveis, acessíveis, resilientes e sustentáveis, e com a Agenda 2030 da ONU e seus Objetivos de Desenvolvimento Sustentável (ODS).</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PMMA.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Conservação e Recuperação da Mata Atlântica</h2>
                  <p class="card__snippet">O Plano Municipal de Conservação e Recuperação da Mata Atlântica (PMMA), criado pela Lei da Mata Atlântica, é um instrumento legal que permite que os municípios atuem na preservação dessa vegetação. Integrado ao Plano Diretor Estratégico (PDE) de São Paulo, o PMMA foi desenvolvido pela Prefeitura em colaboração com várias entidades. O plano define ações prioritárias e áreas para conservação, manejo e recuperação da Mata Atlântica na cidade, com base em mapeamentos de remanescentes vegetais. Ele promove experimentos tecnológicos sustentáveis e a gestão que equilibra a conservação ambiental com o desenvolvimento econômico e cultural. Além disso, incentiva a participação cidadã na gestão pública e inclui ações como educação ambiental, gestão de resíduos sólidos e ecoturismo. O PMMA também fornece subsídios para outras políticas e programas municipais, como saneamento básico, desenvolvimento rural sustentável e o próprio PDE.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PMSA.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Conservação e Recuperação de Áreas Prestadoras de Serviços Ambientais</h2>
                  <p class="card__snippet">O Plano Municipal de Serviços Ambientais (PMSA), estabelecido pelo Plano Diretor Estratégico de 2014, oferece diretrizes para conservação e recuperação de áreas que prestam serviços ambientais. Ele promove a proteção e uso sustentável da biodiversidade, vegetação nativa, recursos hídricos, qualidade do ar, entre outros serviços naturais, tanto em áreas urbanas quanto rurais. O objetivo principal é incentivar políticas e iniciativas para conservar e recuperar essas áreas em São Paulo, com objetivos específicos como regulamentar o registro dessas áreas, incorporar conceitos de serviços ecossistêmicos em políticas setoriais e melhorar ações de comando e controle ambiental.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Municipal de Cultura de São Paulo.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Cultura</h2>
                  <p class="card__snippet">O Plano Municipal de Cultura de São Paulo (PMC-SP) é um documento de planejamento de longo prazo para as políticas culturais da cidade. Foi elaborado com base nas três Conferências Municipais de Cultura realizadas em 2004, 2009 e 2013, e em contribuições da consulta pública. O processo de criação envolveu ampla participação social, incluindo audiências públicas regionais e temáticas, além de consulta digital. O PMC-SP faz parte do Sistema Municipal de Cultura, juntamente com o Conselho Municipal de Política Cultural e o Fundo Municipal de Cultura, fortalecendo a participação de São Paulo no Sistema Nacional de Cultura e contribuindo para o Plano Nacional de Cultura e o pacto federativo entre os governos federal, estadual e municipal.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano de Desenvolvimento.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Desenvolvimento Econômico</h2>
                  <p class="card__snippet">O Plano de Desenvolvimento Econômico é uma iniciativa pioneira de planejamento setorial em São Paulo, elaborada pela Secretaria de Desenvolvimento Econômico e Trabalho em colaboração com a sociedade civil e o setor privado. Composto por 5 eixos, 15 diretrizes e 139 ações de curto, médio e longo prazo, o plano busca impulsionar a recuperação econômica da cidade e promover um desenvolvimento sustentável e inclusivo. Identificou-se 10 setores estratégicos que concentram a maior parte dos empregos na capital, como comércio, economia verde, educação, infraestrutura, saúde, tecnologia e turismo. Propõe-se a colaboração entre todas as secretarias municipais, órgãos públicos, setor privado e sociedade para executar uma estratégia integrada, visando identificar vocações regionais, obras públicas necessárias, desburocratização, qualificação da mão de obra, geração de renda e promoção da cultura.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Plano Municipal de Educação - pme.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Educação</h2>
                  <p class="card__snippet">O Plano Municipal de Educação (PME) é um planejamento participativo com duração de 10 anos, construído por meio de amplo debate com a sociedade. O atual PME, em vigor até 2025, estabelece 13 metas e 14 diretrizes para orientar o planejamento educacional na cidade de São Paulo. Entre as metas estão a ampliação do investimento público em educação, a garantia de uma relação adequada entre alunos e professores, e o fomento à qualidade da Educação Básica. As diretrizes incluem a superação do analfabetismo, a universalização do acesso à escola e a promoção da cidadania e da igualdade educacional. Uma das metas do PME era a elaboração dos Planos Regionais de Educação, processo concluído em 2018, cujos documentos podem ser acessados no site da Secretaria Municipal da Educação.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Plano Municipal de Educação em DH.jpg" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Educação em Direitos Humanos</h2>
                  <p class="card__snippet">O Plano Municipal de Educação em Direitos Humanos (PMEDH) é uma extensão do Plano Nacional de Educação em Direitos Humanos (PNEDH) e uma estratégia para fortalecer o artigo 2º do Plano Municipal de Educação (PME). Resultado de um processo de construção e consolidação de políticas públicas municipais entre 2013 e 2016, o PMEDH é elaborado pela Coordenação de Educação em Direitos Humanos da SMDHC. O plano representa uma síntese de esforços institucionais e intersecretariais, institucionalizando e consolidando ações e políticas públicas municipais de educação em direitos humanos. Estruturado em eixos, abrange diversas dimensões dos direitos humanos na cidade de São Paulo, tornando-se um compromisso da Administração Pública Municipal tanto para cidadãos quanto para servidores. Além de ser um documento jurídico, o PMEDH reflete o compromisso do Estado com os direitos humanos em suas atribuições constitucionais e legais. Refletindo a diversidade e os desafios da cidade, convoca servidores e cidadãos a contribuir para fortalecer a democracia e a cultura de respeito aos direitos humanos. O trabalho para construir uma cultura de direitos humanos requer ações intersecretariais e colaboração entre sociedade civil, governo e movimentos sociais, rumo a uma sociedade mais livre, justa, igualitária e solidária.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo -Plano Municipal de Enfrentamento a Violência Sexual contra Crianças e  Adolescentes.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Enfrentamento a Violência  Sexual contra Crianças e Adolescentes</h2>
                  <p class="card__snippet">O plano tem como objetivo traçar metas e estratégias que, transformadas em ações, promoverão politicas publicas efetivas para prevenção da violência sexual contra crianças e adolescentes, além de qualificar o atendimento de forma integrada no Município, de forma a não revitimizar as crianças e adolescentes e contribuir para a defesa dos direitos e responsabilização dos casos no Município. É um instrumento técnico-político, que visa contribuir para assegurar os direitos e a proteção das crianças e adolescentes contra qualquer tipo de violência sexual, e tem dupla função: ser um guia para a atuação do poder público, da sociedade e das famílias, corresponsáveis em assegurar a efetivação dos direitos de crianças e adolescentes e ser uma ferramenta de acompanhamento e controle dessa atuação, uma vez que dispõe sobre as metas e estratégias necessárias para o cumprimento de seus eixos estratégicos.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Municipal de Erradicação.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Erradicação do Trabalho Infantil e Proteção ao Jovem Trabalhador</h2>
                  <p class="card__snippet">O Município de São Paulo enfrenta desafios na resposta à demanda relacionada ao trabalho infantil, evidenciando fragmentação de iniciativas e deficiência na capacitação dos profissionais. O Plano Municipal de Prevenção e Erradicação do Trabalho Infantil e Proteção ao Adolescente Trabalhador foca em cinco áreas de ação: 1. Superar o subregistro do trabalho infantil, 2. Tornar visíveis as condições de trabalho desprotegido dos adolescentes, 3. Coordenar iniciativas governamentais, 4. Estabelecer interação entre órgãos públicos, e 5. Capacitar profissionais para lidar com o problema. O plano busca uma intervenção articulada e intersetorial para prevenir e erradicar o trabalho infantil na cidade.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PMELSP_page-0001.jpg" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Esportes e Lazer.</h2>
                  <p class="card__snippet">Este Plano Municipal é um componente estratégico para estruturar políticas públicas que promovam a cultura esportiva e de lazer na cidade de São Paulo, consolidando-se como direitos sociais. Valoriza a acessibilidade, intergeracionalidade, multidisciplinaridade, intersetorialidade e descentralização, visando democratizar o acesso à prática esportiva e fomentar condições para o lazer. Assim, o esporte, a atividade física e as práticas de lazer devem ser fortalecidos para que, ao serem incorporados à vida cotidiana dos cidadãos em diferentes etapas da vida, atuem como elementos de integração social, desenvolvimento humano e promoção da saúde. Sobretudo, busca capacitar o cidadão para o exercício da cidadania esportiva e de lazer.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Municipal de Estratégias e Ações Locais pela Biodiversidade.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Estratégias e Ações Locais pela Biodiversidade da Cidade de São Paulo</h2>
                  <p class="card__snippet">A Secretaria do Verde e do Meio Ambiente (SVMA) defende novos paradigmas de sustentabilidade, mas reconhece a necessidade de outras áreas da administração pública municipal incorporarem esses conceitos. Por isso, foi formulado o Plano Municipal de Estratégias e Ações Locais pela Biodiversidade pelo Grupo de Trabalho sobre Biodiversidade (GTB), instituído pela Portaria nº 057/SVMA-G/2009. Este plano estabelece metas e responsáveis para cada ação, contando com a participação de parceiros de outras secretarias municipais, órgãos de governo e universidades. A implementação do plano é promovida pela Portaria nº 91/SVMA-G/2011, e o documento completo está disponível no livro "Ações pela Biodiversidade da Cidade de São Paulo", publicado em julho de 2011.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/plano-de-habitacao-SP.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Habitação</h2>
                  <p class="card__snippet">O Plano Municipal de Habitação tem como objetivo servir como um guia para coordenar a política habitacional e monitorar seus resultados. A partir de um diagnóstico das necessidades habitacionais atuais e suas projeções futuras, o plano identifica os instrumentos, recursos e órgãos envolvidos no atendimento dessas demandas, além de propor programas alinhados com as diretrizes da política habitacional estabelecidas pelo Plano Diretor Estratégico. O plano estabelece metas e prioridades de atendimento até 2012 e apresenta o Plano de Ação da Secretaria de Habitação e Desenvolvimento Urbano da gestão municipal atual.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Municipal de Políticas para Imigrantes.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Políticas para Imigrantes</h2>
                  <p class="card__snippet">A 2ª Conferência Municipal de Políticas para Imigrantes, realizada em novembro de 2019, é fruto de um consolidado processo de construção de políticas públicas entre a Secretaria Municipal de Direitos Humanos (SMDHC) e a sociedade civil. Organizado pelo Conselho Municipal de Imigrantes (CMI), pela Comissão Organizadora (COM) e pela SMDHC, o evento reuniu mais de 800 pessoas e teve, como um de seus resultados, 78 propostas finais aprovadas. Um dos cinco objetivos definidos para a 2ª Conferência Municipal de Políticas para Imigrantes foi “propor bases para a criação de um Plano Municipal”. Sob este marco, o Plano tem como objetivo servir de instrumento de planejamento e implementação de ações concretas, intersetoriais, transversais e transparentes para a Prefeitura de São Paulo, durante o período de 2021-2024, conforme os princípios e diretrizes da Política Municipal para a População Imigrante. A matriz do Plano é composta por 8 Eixos, com objetivos estratégicos e 80 ações prioritárias, compostas por indicadores (incluindo Linha de Base), metas e atores responsáveis, bem como referências legais da Política Municipal para Imigrantes e da 2ª Conferência de Políticas para Imigrantes. Além disso, o documento conta com uma seção específica sobre o processo de monitoramento e avaliação.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/2.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Promoção da Igualdade Racial</h2>
                  <p class="card__snippet">O Plano Municipal de Promoção da Igualdade Racial (PLAMPIR), estabelecido pelo Decreto nº 58 em novembro de 2018, tem como principal objetivo reduzir as disparidades étnico raciais na cidade de São Paulo, com foco na população negra e nos povos indígenas. O Conselho Municipal de Promoção da Igualdade Racial é responsável por avaliar e monitorar a implementação do PLAMPIR, enquanto a Secretaria Municipal de Direitos Humanos e Cidadania, por meio da Coordenação de Promoção da Igualdade Racial, coordena as ações e a articulação institucional necessárias para sua execução.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Municipal de Erradicação.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Saneamento Básico</h2>
                  <p class="card__snippet">A Lei 14.934 de 18/06/2009 autoriza o Poder Executivo Municipal de São Paulo a celebrar contratos e convênios com o Estado e empresas vinculadas para oferecer serviços de abastecimento de água e esgotamento sanitário. O artigo 13 dessa lei exige a apresentação do Plano Municipal de Saneamento Básico. A versão inicial desse plano não visa detalhar todas as ações, mas sim estabelecer diretrizes e estratégias para sua elaboração. Dada a natureza integradora do plano, é necessário considerar as políticas, programas e ações específicas já definidas por outros órgãos públicos.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PMS.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Saúde</h2>
                  <p class="card__snippet">O Plano Municipal de Saúde (PMS) é o principal instrumento de planejamento para definir e implementar as iniciativas de saúde ao longo de um período de quatro anos. Ele apresenta os compromissos do governo na área da saúde, com base em uma análise das necessidades de saúde da população e das particularidades locais. O PMS estabelece diretrizes, objetivos e metas de médio prazo, orientando as ações a serem realizadas nas Programações Anuais de Saúde. O plano é elaborado no primeiro ano de cada gestão e executado a partir do segundo ano até o primeiro ano da gestão seguinte, em alinhamento com outros instrumentos de planejamento governamental, como o Plano Plurianual (PPA) e o Programa de Metas.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PLATUM.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal de Turismo</h2>
                  <p class="card__snippet">Com a criação da Secretaria Municipal de Turismo e o processo de formulação do novo Plano de Turismo Municipal, a gestão pública no turismo foi repensada. O papel do Plano Municipal de Turismo (Platum) foi reforçado na promoção do desenvolvimento econômico, social e cultural, alinhado ao compromisso da Prefeitura de São Paulo com os Objetivos do Desenvolvimento Sustentável da ONU. Houve uma crescente demanda por ações específicas voltadas para os munícipes, incluindo campanhas de valorização da oferta turística da cidade e a inclusão social e produtiva em projetos de turismo. A missão da Política Municipal de Turismo é posicionar a promoção, apoio e execução de projetos turísticos como estratégia de desenvolvimento sustentável da cidade e seus habitantes.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/PMLLB.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal do Livro, Leitura, Literatura e Biblioteca</h2>
                  <p class="card__snippet">O PMLLLB estabelece políticas públicas para o livro, leitura, literatura e bibliotecas, garantindo recursos e acesso, promovendo integração entre escolas, bibliotecas e outros espaços literários. Visa ainda apoiar a criação literária, promover debates, formar mediadores e estimular a economia do livro. Também busca garantir políticas e equipamentos em todas as regiões, além de promover literatura não hegemônica, como a marginal, de mulheres, negros e LGBTs.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - Plano Municipal pela Primeira Infância.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Municipal pela Primeira Infância</h2>
                  <p class="card__snippet">O Plano Municipal pela Primeira Infância (PMPI) de São Paulo é um documento que estabelece diretrizes, metas e ações para crianças de 0 a 6 anos até 2030. Com um período de 12 anos, o plano orientará várias administrações municipais e envolve a responsabilidade compartilhada de diferentes partes, não apenas do poder público. É um plano para a cidade, não ligado a uma gestão específica.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PPA.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Plano Plurianual</h2>
                  <p class="card__snippet">O principal instrumento de planejamento orçamentário de médio prazo do Governo Municipal é o Plano Plurianual (PPA). Ele define as diretrizes, os objetivos e as metas da administração pública federal, contemplando as despesas de capital (como, por exemplo, os investimentos) e outras delas decorrentes, além daquelas relativas aos programas de duração continuada. O PPA é estabelecido por lei, com vigência de quatro anos. Ele se inicia no segundo ano de mandato de um presidente e se prolonga até o final do primeiro ano do mandato de seu sucessor.</p>
                  <a href="" class="card__button">Veja Mais</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item acordeon">
      <div class="marcacao">
        <div class="escopo">
          <div class="container">
            <div class="card_fixo">
              <figure class="card__thumb">
                <img src="../assets/images/Logo - PDM.png" alt="Picture by David Monje" class="card__image">
                <figcaption class="card__caption">
                  <h2 class="card__title">Programa de Metas</h2>
                  <p class="card__snippet">Trata-se de um plano elaborado pelo Prefeito do Município que contém as ações estratégicas, os indicadores e as metas quantitativas para cada um dos setores da Administração Pública Municipal, Subprefeituras e Distritos da cidade, observando, no mínimo, as diretrizes de sua campanha eleitoral e os objetivos, as diretrizes, as ações estratégicas e as demais normas da lei do Plano Diretor Estratégico.</p>
                  <a href="" class="card__button">Veja Mais.</a>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="item">
    </div>
    <div class="item">
    </div>
  </div>
  <div class="controls">
      <div class="first"><i class="fa-solid fa-angles-left"></i></div>
      <div class="prev"><i class="fa-solid fa-arrow-left"></i></div>
      <div class="numbers">
          <div>1</div>
      </div>
      <div class="next"><i class="fa-solid fa-arrow-right"></i></div>
      <div class="last"><i class="fa-solid fa-angles-right"></i></div>
  </div>
</div>
<script src="../assets/js/navegacao.js"></script>'''
    
    
soup = BeautifulSoup(html, 'html.parser')


resultados = []

# Itera sobre cada item com a classe 'item acordeon'
for item in soup.find_all('div', class_='item acordeon'):
    # Busca o título do plano
    titulo = item.find('h2', class_='card__title')
    nome_do_plano = titulo.text if titulo else None

    # Busca a descrição do plano
    snippet = item.find('p', class_='card__snippet')
    desc_plano = snippet.text if snippet else None

    # Busca o caminho da imagem do plano
    imagem = item.find('img')
    logo_plano = imagem['src'] if imagem else None

    # Adiciona os resultados à lista, se todos os elementos forem encontrados
    if nome_do_plano and desc_plano and logo_plano:
        resultados.append({
            'nome_do_plano': nome_do_plano,
            'desc_plano': desc_plano,
            'logo_plano': logo_plano
        })

# Cria um arquivo YAML com os resultados
with open('dados_planos.yml', 'w', encoding='utf-8') as file:
    yaml.dump(resultados, file, default_flow_style=False, allow_unicode=True)