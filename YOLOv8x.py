from ultralytics import YOLO

def main():
    # Carrega o modelo YOLOv8x pré-treinado
    model = YOLO("yolov8x.pt")

    # Treinamento
    model.train(
        data="caminho/para/seu/data.yaml",
        epochs=50,
        imgsz=416,
        batch=16,
        optimizer='SGD',
        device=0,
        name="yolov8x_rural",
        project="resultados_yolo"
    )

if __name__ == "__main__":
    main()

