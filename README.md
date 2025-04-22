# Modelos YOLOv5 e YOLOv8 para Detecção de Objetos em Áreas Rurais

Este repositório acompanha o artigo **"Modelos YOLOv5 e YOLOv8 para Detecção de Objetos em Áreas Rurais"**, que apresenta um estudo comparativo entre os modelos de detecção de objetos **YOLOv5x** e **YOLOv8x** aplicados ao contexto de imagens de áreas rurais.

---

## 📜 Descrição

Este trabalho avalia os modelos **YOLOv5x** e **YOLOv8x** em tarefas de detecção em tempo real em cenários rurais, como a identificação de carro, casa, cafezal, mata, estrada entre outros. Também é explorado o uso da **transferência de aprendizado** para alcançar bons resultados mesmo com datasets menores e limitação de recursos computacionais.

---

## 🧪 Como usar os scripts

Os arquivos `YOLOv5x.py` e `YOLOv8x.py` contêm scripts simples para treinar os modelos. Exemplo:

```python
from ultralytics import YOLO

def main():
    # Carrega o modelo YOLOv8x pré-treinado
    model = YOLO("yolov8x.pt")

    # Treinamento
    model.train(
        data="caminho/para/seu/data.yaml",
        epochs=100,
        imgsz=416,
        batch=16,
        optimizer='SGD',
        device=0,
        name="yolov8x_rural",
        project="resultados_yolo"
    )

if __name__ == "__main__":
    main()
```

> **Importante**: O otimizador utilizado nos experimentos foi o `SGD`, mas você pode alterá-lo para `Adam` ou outro conforme sua aplicação.

---

## 📦 Requisitos

Antes de executar os scripts, instale a biblioteca necessária:

```bash
pip install ultralytics
```

---

## 🗂️ Dataset

O dataset utilizado está disponível no Roboflow, com o nome:

🔗 **[Deteccao Area Rural - Roboflow](https://app.roboflow.com/instituto-nacional-de-telecomunicaes)**

> ⚠️ **Nota**: Esta versão disponível **não é exatamente a utilizada no artigo**, pois foram feitas modificações ao longo do tempo. No entanto, ela contém uma quantidade considerável de imagens rotuladas que podem ser úteis para projetos semelhantes.

### 📥 Como exportar do Roboflow:

1. Acesse o projeto no Roboflow.
2. Clique em **"Export"**.
3. Escolha o formato `YOLOv5 PyTorch` (compatível com YOLOv5/YOLOv8).
4. Faça o download do zip.
5. Descompacte e aponte `data="caminho/para/data.yaml"` no script.

---

## 🧠 Pesos Treinados Disponíveis

Você pode usar os modelos já treinados diretamente:

- 🔵 [YOLOv5x Treinado](https://drive.google.com/drive/folders/176gRY3fRA47eIHWEoyqNOe-jm5M5fexg?usp=sharing)
- 🔴 [YOLOv8x Treinado](https://drive.google.com/drive/folders/1R-2A2X19fHtsMYd5VRxN_QajCgMe8dmc?usp=sharing)

### ▶️ Como usar:

1. Baixe o arquivo `.pt` do link acima.
2. Substitua o caminho do modelo no script:

```python
model = YOLO("caminho/do/modelo.pt")
```

3. Execute normalmente o script para inferência ou avaliação.
