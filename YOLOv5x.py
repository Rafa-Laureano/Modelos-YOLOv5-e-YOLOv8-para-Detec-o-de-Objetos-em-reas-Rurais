from ultralytics import YOLO

def main():
    # Carrega o modelo YOLOv5x pré-treinado
    model = YOLO("yolov5x.pt")

    # Treinamento
    model.train(
        data="caminho/para/seu/data.yaml", # use data.yaml do seu dataset, espera-se formato YOLO
        epochs=50,
        imgsz=416,
        batch=16,
        optimizer='SGD',
        device=0,  # Use 0 para GPU, 'cpu' se não houver
        name="yolov5x_rural",
        project="resultados_yolo"
    )

if __name__ == "__main__":
    main()

