🚗 Plaka Tanıma Sistemi (Plate Recognition System)
Bu proje, bir görüntüdeki araç plakasını tespit etmek ve tanımak için YOLO (You Only Look Once) nesne algılama modelini kullanan bir uygulamadır. Uygulama, kullanıcı dostu bir arayüzle görüntü yükleme ve algılama sonuçlarını görüntüleme imkânı sunan Streamlit kullanılarak geliştirilmiştir.

✨ Temel Özellikler
Plaka Algılama: Yüklenen bir görüntüdeki araç plakalarını otomatik olarak bulur ve konumlandırır.

Akıllı Kırpma: Algılanan plaka alanını kırpar ve daha net görüntülenmesi için ayrı bir görüntü olarak sunar.

Güven Puanı Gösterimi: Her bir algılama için, modelin tahmininden ne kadar emin olduğunu gösteren bir güven puanı sağlar.

Kullanıcı Dostu Arayüz: Sadece birkaç tıklamayla kolayca görüntü yükleyebilir ve sonuçları görebilirsiniz.

🧠 Model Eğitimi
Bu sistemin kalbinde, özel olarak eğitilmiş bir YOLOv8 modeli olan plate_detection.pt bulunmaktadır. Modelin eğitim süreci aşağıdaki adımları içerir:

Veri Toplama: Araç plakası içeren çeşitli görüntülerden oluşan bir veri kümesi oluşturuldu.

Etiketleme (Annotation): Her bir araç plakasının etrafı, modelin doğru bir şekilde öğrenmesi için sınırlayıcı kutularla işaretlendi.

Model Eğitimi: Etiketlenen veri kümesi kullanılarak YOLOv8 modeli eğitildi, böylece model plakaların özelliklerini tanıyabilir hale geldi.

🛠️ Nasıl Çalışır?
Uygulama, main.py ve helper.py olmak üzere iki ana Python dosyasından oluşur:

main.py: Bu dosya, Streamlit ile oluşturulan arayüzü yönetir. Kullanıcının dosya yüklemesini sağlar ve sonuçları görüntüler.

helper.py: Bu dosya, plaka algılama mantığını içerir. YOLO modelini kullanarak görüntüleri işler ve algılama sonuçlarını döndürür.

📦 Kurulum ve Çalıştırma
Bağımlılıklar
Uygulamayı çalıştırabilmek için aşağıdaki kütüphanelerin yüklü olması gerekir:

streamlit

opencv-python

ultralytics

Pillow

numpy

Tüm bağımlılıkları tek bir komutla kurabilirsiniz:

Bash

pip install streamlit opencv-python ultralytics Pillow numpy
Kullanım
Bu depoyu bilgisayarınıza klonlayın.

plate_detection.pt adlı eğitilmiş model dosyasının models klasöründe bulunduğundan emin olun.

Terminalinizi açın ve projenin ana dizinine gidin.

Aşağıdaki komutu çalıştırarak uygulamayı başlatın:

Bash

streamlit run main.py
Web tarayıcınızda otomatik olarak açılan sayfada uygulamayı kullanmaya başlayabilirsiniz.
