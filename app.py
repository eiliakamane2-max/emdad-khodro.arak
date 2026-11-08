from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>خودروبر و امداد خودرو کف خودرو | ۲۴ ساعته</title>
        <style>
            /* تنظیمات کلی */
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: Tahoma, Arial, sans-serif; background-color: #f8f9fa; color: #333; scroll-behavior: smooth; padding-bottom: 80px; overflow-x: hidden; }
            
            /* هدر سایت */
            header { background-color: #009688; color: white; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }
            
            /* لوگوی متنی + آیکون */
            .logo-area { display: flex; align-items: center; gap: 10px; }
            .logo-icon { width: 40px; height: 40px; fill: #ffeb3b; }
            .text-logo { background-color: #00796b; border: 2px solid #ffeb3b; border-radius: 8px; padding: 5px 15px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.3); }
            .text-logo h1 { color: #ffeb3b; font-size: 20px; margin: 0; font-weight: bold; line-height: 1.2; }
            .text-logo span { color: white; font-size: 10px; display: block; margin-top: 2px; }
            
            /* منوی دسکتاپ */
            header nav { display: flex; }
            header nav a { color: white; text-decoration: none; margin-left: 20px; font-size: 16px; transition: 0.3s; font-weight: bold; }
            header nav a:hover { color: #ffeb3b; }
            
            /* منوی موبایل (سه خط) */
            .menu-icon { display: block; font-size: 35px; cursor: pointer; }
            .mobile-menu { display: none; flex-direction: column; background-color: #00796b; position: absolute; top: 80px; right: 0; width: 100%; z-index: 999; box-shadow: 0 5px 10px rgba(0,0,0,0.2); }
            .mobile-menu a { padding: 15px; color: white; text-decoration: none; border-bottom: 1px solid #009688; text-align: center; font-weight: bold; }
            .mobile-menu a:hover { background-color: #009688; }

            /* بخش هیرو */
            .hero { background: linear-gradient(rgba(0, 150, 136, 0.8), rgba(0, 0, 0, 0.7)), url('/static/1.jpg') center/cover; color: white; text-align: center; padding: 140px 20px; border-bottom: 5px solid #ffeb3b; }
            .hero h2 { font-family: 'B Nazanin', 'Tahoma', Arial, sans-serif; font-size: 55px; font-weight: bold; margin-bottom: 20px; color: #fff; text-shadow: 2px 2px 5px rgba(0,0,0,0.7); }
            .hero p { font-size: 20px; margin-bottom: 40px; max-width: 900px; margin-left: auto; margin-right: auto; text-shadow: 1px 1px 3px rgba(0,0,0,0.7); line-height: 1.8; }
            .btn-call { background-color: #ffeb3b; color: #1a1a2e; padding: 18px 45px; font-size: 22px; font-weight: bold; border-radius: 50px; text-decoration: none; display: inline-block; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(255, 235, 59, 0.4); }
            .btn-call:hover { background-color: #fbc02d; transform: translateY(-5px) scale(1.05); }

            /* بخش خدمات */
            .services { padding: 80px 20px; text-align: center; background-color: #ffffff; }
            .services h2 { font-size: 38px; margin-bottom: 50px; color: #1a1a2e; position: relative; display: inline-block; }
            .services h2::after { content: ''; width: 50%; height: 4px; background-color: #009688; position: absolute; bottom: -15px; left: 25%; border-radius: 2px; }
            
            .service-cards { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; max-width: 1200px; margin: 0 auto; }
            .card { background: white; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.08); width: 300px; overflow: hidden; transition: all 0.4s ease; border: 1px solid #eee; display: flex; flex-direction: column; }
            .card:hover { transform: translateY(-15px); box-shadow: 0 15px 30px rgba(0,0,0,0.15); }
            .card img { width: 100%; height: 220px; object-fit: cover; transition: transform 0.4s ease; }
            .card:hover img { transform: scale(1.05); }
            .card-content { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; }
            .card h3 { color: #1a1a2e; font-size: 22px; margin-bottom: 15px; }
            .card p { color: #666; font-size: 15px; line-height: 1.8; flex-grow: 1; }

            /* بخش مزایا (چرا ما) */
            .why-us { background-color: #009688; color: white; padding: 80px 20px; text-align: center; }
            .why-us h2 { font-size: 38px; margin-bottom: 40px; }
            .why-us-desc { max-width: 800px; margin: 0 auto 50px; text-align: right; line-height: 2; font-size: 16px; color: #e0f2f1; }
            .why-us-desc p { margin-bottom: 10px; }

            /* بخش گالری */
            .gallery { padding: 80px 20px; background-color: #ffffff; text-align: center; }
            .gallery h2 { font-size: 38px; margin-bottom: 50px; color: #1a1a2e; position: relative; display: inline-block; }
            .gallery h2::after { content: ''; width: 50%; height: 4px; background-color: #009688; position: absolute; bottom: -15px; left: 25%; border-radius: 2px; }
            
            .gallery-container { display: flex; gap: 20px; overflow-x: auto; padding-bottom: 20px; cursor: grab; scroll-snap-type: x mandatory; }
            .gallery-container::-webkit-scrollbar { height: 8px; }
            .gallery-container::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 10px; }
            .gallery-container::-webkit-scrollbar-thumb { background: #009688; border-radius: 10px; }
            .gallery-container:active { cursor: grabbing; }
            .gallery-container img { height: 250px; width: 350px; object-fit: cover; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); scroll-snap-align: center; user-select: none; -webkit-user-drag: none; }

            /* بخش سوالات متداول */
            .faq { padding: 80px 20px; background-color: #f8f9fa; max-width: 800px; margin: 0 auto; }
            .faq h2 { text-align: center; color: #009688; font-size: 38px; margin-bottom: 40px; }
            .faq-item { background: #fff; margin-bottom: 15px; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
            .faq-question { width: 100%; text-align: right; background: #fff; border: none; padding: 20px; font-size: 18px; font-weight: bold; color: #333; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: Tahoma; transition: 0.3s; }
            .faq-question:hover { background: #e0f2f1; color: #009688; }
            .faq-answer { padding: 20px; display: none; background: #fafafa; color: #555; line-height: 1.8; border-top: 1px solid #eee; }
            
            /* بخش تماس */
            .contact-section { background-color: #e0f2f1; color: #333; padding: 80px 20px; text-align: center; border-top: 5px solid #009688; }
            .contact-section h2 { color: #009688; font-size: 38px; margin-bottom: 20px; }
            .phone-number { font-size: 55px; font-weight: bold; color: #009688; margin: 30px 0; letter-spacing: 3px; direction: ltr; }
            
            .form-container { background-color: #ffffff; padding: 40px; border-radius: 15px; display: inline-block; margin-top: 30px; width: 100%; max-width: 600px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
            .form-container input { width: 100%; padding: 15px; margin: 10px 0; border-radius: 8px; border: 1px solid #ccc; background-color: #f9f9f9; color: #333; font-family: Tahoma; font-size: 16px; transition: 0.3s; }
            .form-container input:focus { border-color: #009688; outline: none; box-shadow: 0 0 8px rgba(0,150,136,0.3); }
            .form-container button { background-color: #009688; color: white; font-weight: bold; border: none; padding: 18px; font-size: 18px; border-radius: 8px; cursor: pointer; width: 100%; transition: 0.3s; margin-top: 10px; }
            .form-container button:hover { background-color: #00796b; }

            /* فوتر */
            footer { background-color: #1a1a2e; color: white; padding: 50px 20px 20px; text-align: center; }
            footer h4 { color: #ffeb3b; margin-bottom: 15px; font-size: 24px; }
            footer p { color: #aaa; margin-bottom: 10px; }
            .social-links { margin: 20px 0; }
            .social-links a { color: white; font-size: 24px; margin: 0 10px; text-decoration: none; transition: 0.3s; }
            .social-links a:hover { color: #009688; }
            .copyright { border-top: 1px solid #333; padding-top: 20px; margin-top: 20px; font-size: 14px; color: #666; }

            /* دکمه شناور تماس */
            .floating-call { position: fixed; bottom: 30px; left: 30px; background-color: #009688; color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 35px; box-shadow: 0 4px 20px rgba(0, 150, 136, 0.6); text-decoration: none; z-index: 9999; transition: all 0.3s ease; animation: pulse 2s infinite; }
            .floating-call:hover { transform: scale(1.1); background-color: #00796b; }
            
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(0, 150, 136, 0.7); }
                70% { box-shadow: 0 0 0 20px rgba(0, 150, 136, 0); }
                100% { box-shadow: 0 0 0 0 rgba(0, 150, 136, 0); }
            }

            /* انیمیشن اسکرول */
            .hidden { opacity: 0; transform: translateY(50px); transition: all 1s; }
            .show { opacity: 1; transform: translateY(0); }

            /* واکنش‌گرایی */
            @media (max-width: 768px) {
                header nav { display: none; } 
                .hero h2 { font-size: 35px; }
                .hero p { font-size: 16px; }
                .phone-number { font-size: 35px; }
                .gallery-container img { height: 200px; width: 280px; }
                .logo-icon { width: 30px; height: 30px; }
                .text-logo h1 { font-size: 16px; }
                .text-logo span { font-size: 9px; }
            }
        </style>
    </head>
    <body>
        <!-- هدر -->
        <header>
            <div class="logo-area">
                <svg class="logo-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/>
                </svg>
                <div class="text-logo">
                    <h1>کف خودرو</h1>
                    <span>خودروبر اراک</span>
                </div>
            </div>
            <nav>
                <a href="/">خانه</a>
                <a href="#services">خدمات</a>
                <a href="#why-us">مزایای ما</a>
                <a href="#gallery">گالری</a>
                <a href="#faq">سوالات متداول</a>
                <a href="#contact">درخواست امداد</a>
            </nav>
            <div class="menu-icon" onclick="toggleMenu()">☰</div>
            <div class="mobile-menu" id="mobileMenu">
                <a href="/">خانه</a>
                <a href="#services">خدمات</a>
                <a href="#why-us">مزایای ما</a>
                <a href="#gallery">گالری</a>
                <a href="#faq">سوالات متداول</a>
                <a href="#contact">درخواست امداد</a>
            </div>
        </header>
        <!-- معرفی -->
        <section class="hero hidden">
            <h2>خودروبر و امداد خودرو ۲۴ ساعته در اراک</h2>
            <p>ما با استفاده از خودروبرهای مجهز به سیستم هیدرولیک (کفی) و جرثقیل‌های قدرتمند، خودروی شما را به مقصد می‌رسانیم.</p>
            <a href="#contact" class="btn-call">درخواست خودروبر فوری</a>
        </section>

        <!-- خدمات -->
        <section class="services hidden" id="services">
            <h2>خدمات ما</h2>
            <div class="service-cards">
                <div class="card">
                    <img src="/static/1.jpg" alt="خودروبر کفی">
                    <div class="card-content"><h3>خودروبر (کفی)</h3><p>کف خودروبر به صورت هیدرولیکی پایین آمده و خودرو با امنیت کامل روی آن قرار می‌گیرد.</p></div>
                </div>
                <div class="card">
                    <img src="/static/2.jpg" alt="یدک کش و جرثقیل">
                    <div class="card-content"><h3>یدک‌کش و جرثقیل</h3><p>انتقال خودروهای سبک و سنگین. در صورت نیاز، خودرو با وینچ به صورت ایمن بارگیری می‌شود.</p></div>
                </div>
                <div class="card">
                    <img src="/static/3.jpg" alt="امداد در محل">
                    <div class="card-content"><h3>امداد در محل</h3><p>اگر خودروی شما در جایی گیر کرده، تیم ما در محل حاضر شده و خودرو را خارج می‌کند.</p></div>
                </div>
                <div class="card">
                    <img src="/static/8.jpg" alt="خودرو سوار">
                    <div class="card-content"><h3>خودرو سوار</h3><p>سرویس حمل خودروهای سواری و لوکس با خودرو سوار (کفی) به صورت کاملاً ایمن و تخصصی.</p></div>
                </div>
            </div>
        </section>

        <!-- مزایای استفاده -->
        <section class="why-us hidden" id="why-us">
            <h2>مزایای استفاده از خدمات خودروبر اراک:</h2>
            <div class="why-us-desc">
                <p>۱. جلب رضایت مشتریان عزیز اولویت کار این مجموعه است.</p>
                <p>۲. خدمات خودروبر با استفاده از سیستم GPS انجام می‌شود.</p>
                <p>۳. این مجموعه در تمام روز هفته و در ۲۴ ساعت شبانه روز آماده خدمت رسانی است.</p>
                <p>۴. کیفیت خدمات امداد رسانی در مجموعه خودروبر اراک بسیار بالاست.</p>
                <p>۵. خدمات امداد رسانی و حمل خودرو با سرعت و ظرافت بالا انجام می‌گیرد.</p>
                <p style="margin-top: 20px;">حمل خودرو با خودروبر، حمل خودرو با یدک کش، حمل خودرو با جرثقیل، حمل خودرو با خودروسوار، پوشش تمام مناطق شهری و بین شهری، شفافیت در خدمات و کیفیت خدمات، به صورت شبانه روزی، بالاترین سطح کیفیت، جرثقیل اراک، خدمات حمل خودروی های خارجی با یدک کش مانند خودروی...</p>
            </div>
        </section>

        <!-- گالری تصاویر -->
        <section class="gallery hidden" id="gallery">
            <h2>تصاویری از کارهای ما</h2>
            <div class="gallery-container" id="gallery-container">
                <img src="/static/4.jpg" alt="کار 4">
                <img src="/static/5.jpg" alt="کار 5">
                <img src="/static/6.jpg" alt="کار 6">
                <img src="/static/7.jpg" alt="کار 7">
                <img src="/static/8.jpg" alt="کار 8">
            </div>
        </section>

        <!-- سوالات متداول -->
        <section class="faq hidden" id="faq">
            <h2>سوالات متداول</h2>
            <div class="faq-item">
                <button class="faq-question">تفاوت یدک‌کش و خودروبر چیست؟</button>
                <div class="faq-answer">یدک‌کش خودرو را با زاویه بالا می‌کشد اما خودروبر (کفی) خودرو را کاملاً صاف حمل می‌کند که برای مسافت‌های طولانی و خودروهای اتوماتیک بهترین گزینه است.</div>
            </div>
            <div class="faq-item">
                <button class="faq-question">هزینه حمل خودرو چگونه محاسبه می‌شود؟</button>
                <div class="faq-answer">هزینه بر اساس مسافت، نوع خودرو و شرایط جاده محاسبه می‌شود. برای قیمت دقیق با ما تماس بگیرید.</div>
                </div>
            <div class="faq-item">
                <button class="faq-question">چه مدت طول می‌کشد تا خودروبر برسد؟</button>
                <div class="faq-answer">زمان رسیدن بستگی به ترافیک و موقعیت مکانی شما دارد، اما تیم ما معمولاً در کوتاه‌ترین زمان ممکن (بین ۱۵ تا ۳۰ دقیقه در سطح شهر) در محل حاضر می‌شود.</div>
            </div>
            <div class="faq-item">
                <button class="faq-question">آیا برای حمل خودروهای خارجی و لوکس هم خدمات دارید؟</button>
                <div class="faq-answer">بله، مجموعه ما با استفاده از خودروبرهای کفی مجهز و تسمه‌بندی ایمن، آماده حمل خودروهای خارجی و لوکس با بالاترین سطح کیفیت و بدون هیچ‌گونه آسیبی است.</div>
            </div>
        </section>

        <!-- تماس با ما -->
        <section class="contact-section hidden" id="contact">
            <h2>درخواست خودروبر فوری</h2>
            <p>برای تماس فوری با ما روی شماره‌های زیر بزنید:</p>
            <div class="phone-number">0918-218-3872</div>
            <div class="phone-number">0918-160-3872</div>
            
            <div class="form-container">
                <form method="POST" action="/">
                    <input type="text" name="name" placeholder="نام و نام خانوادگی" required>
                    <input type="tel" name="phone" placeholder="شماره تماس شما" required>
                    <input type="text" name="problem" placeholder="مشکل خودرو را بنویسید" required>
                    <button type="submit">ارسال درخواست</button>
                </form>
            </div>
        </section>

        <!-- فوتر -->
        <footer>
            <h4>خودروبر و امداد خودرو کف خودرو</h4>
            <p>سرویس ۲۴ ساعته، ۷ روز هفته</p>
            <div class="social-links">
                <a href="#">📸</a>
                <a href="#">💬</a>
                <a href="#">📞</a>
            </div>
            <div class="copyright">
                &copy; ۲۰۲۴ تمامی حقوق محفوظ است.
            </div>
        </footer>

        <!-- دکمه شناور تماس -->
        <a href="tel:09182183872" class="floating-call" title="تماس فوری">
            📞
        </a>

        <script>
            // کد باز و بسته کردن منوی موبایل
            function toggleMenu() {
                var menu = document.getElementById("mobileMenu");
                if (menu.style.display === "flex") {
                    menu.style.display = "none";
                } else {
                    menu.style.display = "flex";
                }
            }

            // کد سوالات متداول
            var acc = document.getElementsByClassName("faq-question");
            var i;
            for (i = 0; i < acc.length; i++) {
                acc[i].addEventListener("click", function() {
                    this.classList.toggle("active");
                    var panel = this.nextElementSibling;
                    if (panel.style.display === "block") { panel.style.display = "none"; } 
                    else { panel.style.display = "block"; }
                });
            }

            // کد انیمیشن اسکرول
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('show');
                    }
                });
            });
            const hiddenElements = document.querySelectorAll('.hidden');
            hiddenElements.forEach((el) => observer.observe(el));

            // کد درگ کردن گالری عکس (کلیک و کشیدن با موس)
            const slider = document.getElementById('gallery-container');
            let isDown = false;
            let startX;
            let scrollLeft;

            slider.addEventListener('mousedown', (e) => {
                isDown = true;
                slider.classList.add('active');
                startX = e.pageX - slider.offsetLeft;
                scrollLeft = slider.scrollLeft;
            });
            slider.addEventListener('mouseleave', () => {
                isDown = false;
                slider.classList.remove('active');
            });
            slider.addEventListener('mouseup', () => {
                isDown = false;
                slider.classList.remove('active');
            });
            slider.addEventListener('mousemove', (e) => {
                if (!isDown) return;
                e.preventDefault();
                const x = e.pageX - slider.offsetLeft;
                const walk = (x - startX) * 2;
                slider.scrollLeft = scrollLeft - walk;
            });
        </script>
    </body>
    </html>
    """

@app.route('/', methods=['POST'])
def handle_form():
    name = request.form.get('name')
    phone = request.form.get('phone')
    problem = request.form.get('problem')
    
    return f"""
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>درخواست ثبت شد</title>
        <style>
            body {{ background-color: #009688; color: white; font-family: Tahoma; text-align: center; padding-top: 100px; }}
            h1 {{ color: #ffeb3b; margin-bottom: 20px; }}
            .box {{ background-color: #ffffff; color: #333; padding: 40px; border-radius: 15px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }}
            .info {{ margin: 15px 0; font-size: 18px; color: #555; }}
            strong {{ color: #009688; }}
            a {{ color: #009688; text-decoration: none; font-size: 18px; display: inline-block; margin-top: 20px; border: 2px solid #009688; padding: 10px 20px; border-radius: 5px; transition: 0.3s; font-weight: bold; }}
            a:hover {{ background-color: #009688; color: white; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>✅ درخواست شما ثبت شد!</h1>
            <p class="info"><strong>{name}</strong> عزیز، به زودی با شماره <strong>{phone}</strong> تماس می‌گیریم.</p>
            <p class="info">مشکل خودرو: {problem}</p>
            <a href="/">بازگشت به صفحه اصلی</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)