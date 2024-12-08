import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Настройки за Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
your_email = "mineralhotelinfo@gmail.com"
your_password = "ylnppaqssnyjftcc"

# Имейли на получателите

to_emails = [
    "Lyups.i.a@gmail.com", "t.toni@abv.bg"
]

# Създаване на MIME обект за съобщението
message = MIMEMultipart()
message['From'] = your_email
message['Subject'] = 'Коледни оферти за книги'

# HTML съдържание
html_content = """
<!DOCTYPE html>
<html>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #F0F0F0; color: #000000;">
<div style="display: none; visibility: hidden; opacity: 0; height: 0; max-height: 0; overflow: hidden; color: transparent;">
    🎁 Не пропускай нашите коледни оферти!
</div>

<!-- Wrapper -->
<table width="100%" cellpadding="0" cellspacing="0" style="margin: 0; padding: 0; width: 100%; background-color: #F0F0F0;">
  <tr>
    <td align="center">

      <!-- Main Container -->
      <table width="600" cellpadding="0" cellspacing="0" style="background-color: #FFFFFF; max-width: 600px; width: 100%; margin: 20px auto; border-radius: 8px; overflow: hidden;">

        <!-- Logo -->
        <tr>
          <td align="center" style="padding: 20px;">
            <a href="https://hotel-ognqnovo.pro/?utm_source=email&utm_medium=email&utm_campaign=christmas_basic_offers" target="_blank">
              <img src="https://almishev.github.io/email-marketing/images/logoh.png" alt="Промоции от Книжарница Хеликон" style="max-width: 100px; height: auto; display: block; border: none;">
            </a>
          </td>
        </tr>

        <!-- Header -->
        <tr>
          <td align="center" style="background-color: #ff9206; padding: 10px; color: #FFFFFF; font-size: 18px; font-weight: bold;">
            🎄 Коледни чудеса в света на книгите!
          </td>
        </tr>

        <!-- Subheader -->
        <tr>
          <td align="center" style="padding: 15px; font-size: 16px; color: #000000;">
            Вълшебство под елхата – открий перфектния подарък за всеки любител на книгите! ✨
          </td>
        </tr>

        <!-- Hero Image -->
        <tr>
          <td align="center">
            <a href="https://hotel-ognqnovo.pro/?utm_source=email&utm_medium=email&utm_campaign=christmas_basic_offers" target="_blank">
              <img src="https://almishev.github.io/email-marketing/images/helicon-banner.jpg" alt="Коледна оферта" style="max-width: 100%; height: auto; display: block; border: none;">
            </a>
          </td>
        </tr>

        <!-- CTA Button -->
        <tr>
          <td align="center" style="padding: 20px;">
            <a href="https://hotel-ognqnovo.pro/?utm_source=email&utm_medium=email&utm_campaign=christmas_basic_offers" target="_blank" style="background-color: #ff9206; color: #FFFFFF; padding: 12px 20px; text-decoration: none; font-size: 16px; border-radius: 5px; display: inline-block;">🔎 Разгледай сега</a>
          </td>
        </tr>

        <!-- Divider -->
        <tr>
          <td style="padding: 5px 0;">
            <hr style="border: none; border-top: 1px solid #E0E0E0;">
          </td>
        </tr>

        <!-- Product List -->
        <tr>
          <td style="padding: 5px;">
            <!-- Item 1 -->
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 20px;">
              <tr>
                <td width="30%" align="center" style="padding-right: 10px;">
                  <a href="https://hotel-ognqnovo.pro/?utm_source=email&utm_medium=email&utm_campaign=christmas_song_offers" target="_blank">
                    <img src="https://almishev.github.io/email-marketing/images/koledna-pesen.png" alt="Коледна песен" style="width: 100px; height: auto; display: block;">
                  </a>
                </td>
                <td style="font-size: 14px; color: #000000;">
                  <b style="color: #345cb1;">Коледна песен (Чарлз Дикенс)</b><br/>
                  Историята за Скрудж, Тим и призраците е не просто коледно четиво, а послание да вярваме в доброто и да го отстояваме.
                </td>
              </tr>
            </table>

            <!-- Item 2 -->
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 20px;">
              <tr>
                <td width="30%" align="center" style="padding-right: 10px;">
                  <a href="https://hotel-ognqnovo.pro/?utm_source=email&utm_medium=email&utm_campaign=christmas_redactor_offers" target="_blank">
                    <img src="https://almishev.github.io/email-marketing/images/helikon-redaktor.jpg" alt="Изборът на редактора" style="width: 100px; height: auto; display: block;">
                  </a>
                </td>
                <td style="font-size: 14px; color: #000000;">
                  <b style="color: #345cb1;">Изборът на редактора</b><br/>
                  Нашите редактори са подготвили специална селекция от книги, които ще зарадват всеки любител на четенето.
                </td>
              </tr>
            </table>

            <!-- Item 3 -->
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 0;">
              <tr>
                <td width="30%" align="center" style="padding-right: 10px;">
                  <a href="https://hotel-ognqnovo.pro/?utm_source=email&utm_medium=email&utm_campaign=christmas_vaucher_offers" target="_blank">
                    <img src="https://almishev.github.io/email-marketing/images/vaucher.jpg" alt="Подаръчен ваучер" style="width: 100px; height: auto; display: block;">
                  </a>
                </td>
                
                <td style="font-size: 14px; color: #000000;">
                  <b style="color: #345cb1;">Подаръчен ваучер</b><br/>
                  Не знаете какво да изберете? Подарете ваучер и оставете получателя да избере любимата си книга!
                  
                 </td>
                
              </tr>
             
            </table>
          </td>
        </tr>

        


        <!-- Footer -->
        <tr>
          <td style="padding: 20px; font-size: 14px; text-align: center; color: #888888;">
            Имаш въпроси? Пиши ни на <a href="mailto:service@helikon.bg" style="color: #345cb1;">service@helikon.bg</a>.<br/>
            &copy; 2024 Helikon. Всички права запазени.
          </td>
        </tr>
      </table>
      <!-- End of Main Container -->


      <table border="0" cellpadding="0" cellspacing="0" align="center"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="wrapper">

	<!-- SOCIAL NETWORKS -->
	<!-- Image text color should be opposite to background color. Set your url, image src, alt and title. Alt text should fit the image size. Real image size should be x2 -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 25px;" class="social-icons"><table
			width="256" border="0" cellpadding="0" cellspacing="0" align="center" style="border-collapse: collapse; border-spacing: 0; padding: 0;">
			<tr>

				<!-- ICON 1 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://www.facebook.com/helikon.bg"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="F" title="Facebook"
					width="44" height="44"
					src="https://almishev.github.io/email-marketing/images/social-icons/facebook.png"></a></td>

				<!-- ICON 2 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://www.facebook.com/helikon.bg"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="T" title="Twitter"
					width="44" height="44"
					src="https://almishev.github.io/email-marketing/images/social-icons/twitter.png"></a></td>				

				<!-- ICON 3 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://www.youtube.com/watch?v=3yFv7UHgHtg"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="G" title="Google Plus"
					width="44" height="44"
					src="https://almishev.github.io/email-marketing/images/social-icons/googleplus.png"></a></td>		

				<!-- ICON 4 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://www.instagram.com/helikonbookstore/"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="I" title="Instagram"
					width="44" height="44"
					src="https://almishev.github.io/email-marketing/images/social-icons/instagram.png"></a></td>

			</tr>
			</table>
		</td>
	</tr>
      
	
	<!-- FOOTER -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif"). Duplicate all text styles in links, including line-height -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 14px; font-weight: 400; line-height: 150%;
			padding-top: 20px;
			padding-bottom: 20px;
			color: #345cb1;
			font-family: sans-serif;" class="footer">

"Книгите са кораби на мисълта, които странстват по вълните на времето и грижливо пренасят своя безценен товар от поколение на поколение." - Френсис Бейкън

				<!-- ANALYTICS -->
				<!-- http://www.google-analytics.com/collect?v=1&tid={{G-THECMWJZTK}}&cid={{Client-ID}}&t=event&ec=email&ea=open&cs={{Campaign-Source}}&cm=email&cn={{Christmas gifts}} -->
				<img width="1" height="1" border="0" vspace="0" hspace="0" style="margin: 0; padding: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: block;"
				src="https://www.google-analytics.com/mp/collect?measurement_id=G-THECMWJZTK&api_secret=Ye4BVpzdSampuZ64VkQIWg&client_id=12345&t=event&en=email_opened&ep.campaign=christmas_offers" />

		</td>
	</tr>
</table>

    </td>
  </tr>
</table>
<!-- End of Wrapper -->

</body>
</html>
"""

# Добавяне на HTML съдържание към имейла
message.attach(MIMEText(html_content, "html"))

# Настройване на получателите с Bcc
message['Bcc'] = ', '.join(to_emails)

# Изпращане на имейлите
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Защита на връзката
    server.login(your_email, your_password)
    server.sendmail(your_email, to_emails, message.as_string())
    print("Имейлът беше изпратен успешно до всички получатели.")
except Exception as e:
    print(f"Грешка при изпращането на имейлите: {e}")
finally:
    server.quit()
