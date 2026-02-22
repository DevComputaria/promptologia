# 📖 O Tomo da API (Technical API Spec)

## 📍 Endpoint
`[METODO] /rota/do/endpoint`

## 🔐 Autenticação
[Nenhum / JWT / API Key / OAuth2]

## 📥 Entrada (Request)
### Headers
- `Content-Type: application/json`

### Body
```json
{
  "campo": "exemplo"
}
```

## 📤 Saída (Response)
### Sucesso (200 OK)
```json
{
  "id": 123,
  "status": "sucesso"
}
```

### Erros Possíveis
- **400 Bad Request**: Quando...
- **401 Unauthorized**: Quando...

---
*Que os elétrons fluam com precisão.*
