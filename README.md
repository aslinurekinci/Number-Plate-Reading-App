Plaka Tanıma Sistemi
Bu proje, araç plakalarını görüntülerden tespit etmek ve tanımak için YOLO (You Only Look Once) nesne algılama modelini kullanan bir Plaka Tanıma Sistemi'dir. Uygulama, görüntüleri yüklemek ve algılama sonuçlarını görüntülemek için kullanıcı dostu bir arayüz sağlayan Streamlit ile geliştirilmiştir.

Özellikler
Plaka Algılama: Uygulama, yüklenen bir görüntüdeki araç plakalarını tanımlayabilir ve konumlandırabilir.

Kırpma ve Görüntüleme: Algılamadan sonra, plaka alanı kırpılır ve algılanan plakanın işaretli olduğu orijinal görüntü ile birlikte ayrı olarak gösterilir.

Güven Puanı: Sistem, algılanan her bir plaka için modelin ne kadar emin olduğunu gösteren bir güven puanı sağlar.

Kullanıcı Dostu Arayüz: Web uygulamasının kullanımı basittir; bir görüntü yükleyin ve sonuçları anında görün.

Model Eğitimi
Bu sistemin temelinde, özel olarak eğitilmiş bir YOLOv8 modeli olan plate_detection.pt bulunmaktadır. Eğitim süreci genel olarak şu adımları içerir:

Veri Toplama: İçinde araç plakaları bulunan görüntülerden oluşan bir veri kümesi toplandı.

Etiketleme (Annotation): Görüntülerdeki her bir araç plakası manuel olarak etiketlendi ve etrafına bir sınırlayıcı kutu çizilerek bir eğitim veri seti oluşturuldu.

Eğitim: Etiketlenmiş veriler, araç plakalarının desenlerini ve özelliklerini tanımayı öğrenen YOLOv8 modelini eğitmek için kullanıldı.

Nasıl Çalışır?
Uygulama, iki ana Python betiği kullanır: main.py ve helper.py.

main.py: Bu betik, Streamlit ile oluşturulmuş uygulamanın ön yüzüdür. Dosya yükleyici ve görüntüleri gösterme gibi kullanıcı arayüzü bileşenlerini yönetir. Kullanıcı bir görüntü yüklediğinde, main.py görüntü verilerini detect_plate fonksiyonuna gönderir.

helper.py: Bu betik, plaka algılama için temel mantığı içerir. Yüklenen görüntüyü işlemek için YOLO modelini kullanır. detect_plate fonksiyonu, bir görüntü ve model yolunu girdi olarak alır ve sınırlayıcı kutularla işlenmiş görüntüyü, kırpılmış plakayı ve plaka algılanıp algılanmadığını belirten bir bayrak döndürür.

Bağımlılıklar
Bu uygulamayı çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

streamlit

opencv-python

ultralytics

Pillow

numpy

Hepsini tek seferde pip kullanarak kurabilirsiniz:

Bash

pip install streamlit opencv-python ultralytics Pillow numpy
Kullanım
Bu depoyu bilgisayarınıza klonlayın.

plate_detection.pt model dosyasının models dizininde bulunduğundan emin olun.

Terminalinizden Streamlit uygulamasını çalıştırın:

Bash

streamlit run main.py
Web tarayıcınızda size verilen yerel URL'yi açın.

Bir araç görüntüsü yükleyin, sistem plakayı algılayacak ve gösterecektir.
