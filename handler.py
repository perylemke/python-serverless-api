import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def post(event, context):
    req = json.loads(event['body'])
    num_pessoas = req["pessoas"]
    contas = req["contas"]
    resultado = []
    total_valores = 0
    
    for k, v in contas.items():
        valor_formatado = locale.currency(v['valor']/num_pessoas, grouping=True, symbol=True)
        resultado.append(f"{v['data_vcto']} - {k.title()}: {valor_formatado}")
        total_valores += v['valor']/num_pessoas
        
    total_formatado = locale.currency(total_valores, grouping=True, symbol=True)
    msg = "\n".join(resultado)
    msg += f"\nTotal de Contas: {total_formatado}"
        
    return msg