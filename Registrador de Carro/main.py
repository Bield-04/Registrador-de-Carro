from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --- CONFIGURAÇÃO DO CORS (OBRIGATÓRIO PARA O FRONT-END FUNCIONAR) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer página acesse a API
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, etc.
    allow_headers=["*"],
)

class Carro(BaseModel):
    Marca: str
    Modelo: str
    Ano: str
    Placa: str

lista_de_carros = []
carro1 = Carro(Marca="Hyundai", Modelo="I30", Ano="2010" , Placa= "ABC=123")
lista_de_carros.append(carro1)

@app.get("/")
def Funcionamento():
    return {"status": "O API ta funcionando", "codigo": "0"}

# Nova rota para o front-end puxar a lista de carros atualizada
@app.get("/Carros/")
def listar_carros():
    return lista_de_carros

@app.post("/Carros/")
def registra(carro: Carro):
    lista_de_carros.append(carro)
    return {"mensagem": f"O {carro.Marca} {carro.Modelo} foi registrado com Sucesso"}