from ultralytics import YOLO
import os


def run_batch_inference(model_path, source_folder, output_project='tests', output_name='my_results'):
    if not os.path.exists(model_path):
        print(f"Hata: Model dosyası bulunamadı: {model_path}")
        return

    model = YOLO(model_path)

    print(f"İşlem başlıyor: {source_folder} klasöründeki resimler taranıyor...")

    results = model.predict(
        source=source_folder,
        save=True,
        conf=0.5,
        save_txt=True,
        project=output_project,
        name=output_name,
        exist_ok=True
    )

    print(f"İşlem başarıyla tamamlandı!")
    print(f"Sonuçlar şu klasörde: {os.path.join(output_project, output_name)}")
    return results


if __name__ == "__main__":
    MODEL_FILE = 'runs/detect/train/weights/best.pt'
    IMAGES_DIR = '../images'

    run_batch_inference(MODEL_FILE, IMAGES_DIR)