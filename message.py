
def render_message(date: str) -> (str, str):
    """Generates both, a plain-text version and an html version of the mail and
    returns them in a tuple.
    """

    # Create the plain-text and HTML version of your message
    text = f"""\
    Liebe Community,

    am kommenden Mittwoch ist wieder der erste Mittwoch im Monat. Das heißt:
    *Freifunktreffen auf der c-base*.

    Hier kannst du viele andere Freifunkende Treffen und Kontakte schließen.
    Meistens nutzen wir dieses Treffen, um Community-Themen zu besprechen
    und bei einem leckeren Getränk eine schöne Zeit zu haben. Falls Du Lust
    auf Hardware-Hackereien (z.B. Router-flashen) hast, antworte am besten kurz
    auf diese Mail und schaue, ob auch jemand kommt, der sich mit Dir darum
    kümmern kann.

    *Freifunk-Treffen auf der c-base*
    *Mittwoch, {date}, ab ca. 20 Uhr*
    *Rungestraße 20, 10179 Berlin*

    Die c-base ist an der Spree, ganz in der Nähe vom Bahnhof Jannowitzbrücke.

    https://www.openstreetmap.org/?mlat=52.51297&mlon=13.42011#map=17/52.51297/13.42011

    Du möchtest ein Thema vorschlagen, dass wir als Community besprechen
    sollten? Schicke deinen Themenvorschlag gerne als Antwort auf diese E-Mail.

    Dies ist eine automatische Erinnerung von _CommBot_, deinem freundlichen
    Community-Bot.

    Viele Grüße
    Dein CommBot
    """

    # create html-version
    html = f"""\
    <html>
      <head>

        <meta http-equiv=3D"content-type" content=3D"text/html; charsetUTF-8">
      </head>
      <body>
        <p>Liebe Community,</p>
        <p>am kommenden Mittwoch ist wieder der erste Mittwoch im Monat. Das
          heißt: <b>Freifunktreffen auf der c-base</b>.</p>
        <p>Hier kannst du viele andere Freifunkende Treffen und Kontakte
          schließen. Meistens nutzen wir dieses Treffen, um Community-Themen
          zu besprechen und bei einem leckeren Getränk eine schöne Zeit zu
          haben. Falls Du Lust auf Hardware-Hackereien (z.B. Router-flashen)
          hast, antworte am besten kurz auf diese Mail und schaue, ob auch
          jemand kommt, der sich mit Dir darum kümmern kann.</p>
        <p><b>Freifunk-Treffen auf der c-base<br>
            Mittwoch, {date}, ab ca. 20 Uhr<br>
          </b><b>Rungestraße 20, 10179 Berlin</b></p>
        <p>Die c-base ist an der Spree, ganz in der Nähe vom Bahnhof
          Jannowitzbrücke.</p>
        <p><a href="https://www.openstreetmap.org/?mlat=52.51297&mlon=13.42011#map=17/52.51297/13.42011">Lage auf OpenStreetMap</a></p>
        <p>Du möchtest ein Thema vorschlagen, dass wir als Community
          besprechen sollten? Schicke deinen Themenvorschlag gerne als
          Antwort auf diese E-Mail.<br>
        </p>
        <p>Dies ist eine automatische Erinnerung von <i>CommBot</i>, deinem
          freundlichen Community-Bot.</p>
        <p>Viele Grüße<br>
          Dein CommBot<br>
        </p>
      </body>
    </html>
    """

    return (text, html)
