from ultralytics import YOLO
import torch

def train_with_gpu():

    if not torch.cuda.is_available():
        print("Uyarı: GPU bulunamadı, CPU üzerinden devam ediliyor.")
        device = 'cpu'
    else:
        print(f"GPU Tespit Edildi: {torch.cuda.get_device_name(0)}")
        device = 0

    model = YOLO('yolo26s.pt')


    model.train(
        data='Stop-Sign-1/data.yaml',
        epochs=100,
        imgsz=640,
        device=device,
        batch=16,
        workers=8,
        amp=True
    )

if __name__ == "__main__":
    train_with_gpu()