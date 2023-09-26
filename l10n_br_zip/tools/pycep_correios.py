import json
import logging
import re

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CARACTERES_NUMERICOS = re.compile(r'[^0-9]')
NUMBERS = re.compile(r'[^0-9]')

PRODUCAO = 1
HOMOLOGACAO = 2

URL = {
    HOMOLOGACAO: 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
    PRODUCAO: 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
}

URL_GET_ADDRESS_FROM_CEP = 'http://www.viacep.com.br/ws/{}/json'
URL_GET_CEP_FROM_ADDRESS = 'http://www.viacep.com.br/ws/{}/{}/{}/json'


def format_cep(cep):
    """Formata CEP, removendo qualquer caractere não numérico.

    Arguments:
        cep {str} -- CEP a ser formatado.
    Raises:
        ValueError -- Quando a string esta vazia ou não contem numeros.
    Returns:
        str -- string contendo o CEP formatado.
    """
    if not isinstance(cep, str) or not cep:
        raise ValueError(
            'CEP must be a non-empty string containing only numbers')

    return NUMBERS.sub('', cep)

def get_address_from_cep(cep):
    """Retorna o endereço correspondente ao número de CEP informado.

    Arguments:
        cep {str} -- CEP a ser consultado.
    Raises:
        BaseException -- Quando ocorre qualquer erro na consulta do CEP.
    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    cep = format_cep(cep)

    try:
        response = requests.get(URL_GET_ADDRESS_FROM_CEP.format(cep))

        if response.status_code == 200:
            address = json.loads(response.text)

            if 'error' in address and address['error']:
                pass

            return {
                'bairro': address.get('bairro', ''),
                'cep': address.get('cep', ''),
                'cidade': address.get('localidade', ''),
                'logradouro': address.get('logradouro', ''),
                'uf': address.get('uf', ''),
                'complemento': address.get('complemento', ''),
            }

        elif response.status_code == 400:
            raise exceptions.BaseException(message='Invalid CEP: %s' % cep)  # noqa
        else:
            pass

    except requests.exceptions.RequestException as e:
        pass
