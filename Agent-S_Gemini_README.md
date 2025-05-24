# شرح تشغيل Agent-S المعدل (مع Gemini API)

تم تعديل وكيل Agent-S ليعمل حصرياً باستخدام Google Gemini API بناءً على طلبك. يوضح هذا الدليل كيفية إعداد وتشغيل النسخة المعدلة.

## المتطلبات الأساسية

1.  **Python:** تأكد من تثبيت Python 3.11 أو أحدث.
2.  **Pip:** مدير حزم Python (عادةً ما يأتي مع Python).
3.  **Git:** لتنزيل المستودع (إذا لم تكن تستخدم الملفات المرفقة مباشرة).
4.  **مكتبات Python:**
    *   المكتبات الموجودة في `requirements.txt`.
    *   مكتبة Gemini API: `google-generativeai`.
5.  **(اختياري - لتشغيل cli_app.py):** بيئة سطح مكتب رسومية (مثل Windows, macOS, أو Linux مع X11/Wayland). يتطلب `cli_app.py` مكتبة `pyautogui` التي تحتاج إلى شاشة للعمل.

## الإعداد

1.  **الحصول على الكود:**
    *   إذا كنت تستخدم الملفات المرفقة، انتقل إلى الخطوة 2.
    *   أو، قم بتنزيل المستودع الأصلي وانسخ الملف المعدل `gui_agents/s2/core/engine.py` فوق الملف الأصلي.
        ```bash
        git clone https://github.com/simular-ai/Agent-S.git
        cd Agent-S
        # انسخ الملف engine.py المعدل إلى gui_agents/s2/core/
        ```

2.  **تثبيت المتطلبات:**
    *   افتح الطرفية (Terminal) في مجلد `Agent-S`.
    *   قم بتثبيت المتطلبات الأساسية:
        ```bash
        pip3 install -r requirements.txt
        ```
    *   قم بتثبيت مكتبة Gemini:
        ```bash
        pip3 install google-generativeai
        ```

3.  **مفتاح Gemini API:**
    *   تم تضمين مفتاح Gemini API الذي قدمته (`AIzaSy...maHA`) مباشرة في ملف `gui_agents/s2/core/engine.py`.
    *   **ملاحظة:** لأمان أفضل، يفضل استخدام متغيرات البيئة أو وسيطات سطر الأوامر لتمرير المفتاح بدلاً من تضمينه في الكود مباشرة إذا قمت بتعديلات مستقبلية.

## كيفية التشغيل

### أ. اختبار تكامل Gemini API (بدون واجهة رسومية)

تم إنشاء سكربت `test_gemini_integration.py` (مرفق) للتحقق من أن الاتصال بـ Gemini API يعمل بشكل صحيح دون الحاجة لواجهة رسومية. يمكنك تشغيله كالتالي من داخل مجلد المشروع الرئيسي:

```bash
python3.11 /path/to/test_gemini_integration.py
```
(استبدل `/path/to/` بالمسار الصحيح للسكربت إذا لم يكن في المجلد الحالي).

### ب. تشغيل واجهة سطر الأوامر (CLI App - يتطلب واجهة رسومية)

لتشغيل الوكيل عبر سطر الأوامر للتفاعل مع سطح المكتب (إذا كنت في بيئة رسومية):

1.  انتقل إلى مجلد `Agent-S` في الطرفية.
2.  قم بتشغيل الأمر التالي:

    ```bash
    python3.11 gui_agents/s2/cli_app.py --provider "gemini" --model "gemini-1.5-flash" --grounding_model_provider "gemini" --grounding_model "gemini-1.5-flash" --embedding_engine_type "gemini"
    ```

    *   هذا الأمر يحدد Gemini كمزود ونموذج لجميع المكونات (التوليد الرئيسي، التأسيس Grounding، والتضمين Embedding).
    *   **تذكير:** سيفشل هذا الأمر إذا لم تكن في بيئة تحتوي على خادم عرض (Display Server) بسبب اعتماد `pyautogui`.

## ملاحظات هامة

*   تم تعديل الملف `gui_agents/s2/core/engine.py` بشكل أساسي لإزالة دعم OpenAI و Anthropic والاعتماد حصرياً على Gemini API، وتحديث الكود ليتوافق مع أحدث إصدار من مكتبة `google-generativeai`.
*   تم حل مشاكل الاستيراد والتوافق التي ظهرت أثناء التعديل.
*   تم التحقق من نجاح الاتصال بـ Gemini API باستخدام مفتاحك عبر سكربت اختبار مستقل.

