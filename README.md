<h1>CodExpress — Nivel Básico (Fundamentos y Lógica)</h1>
<p><strong>Tiempo total:</strong> 3 horas · <strong>Objetivo:</strong> completar <u>7 u 8 mini-retos</u> y, si te alcanza el tiempo, una <u>app integrada (código 1900)</u> que reutilice tu propio código.</p>

<h2>¿Cómo trabajamos en este repo?</h2>
<ol>
  <li>Haz <em>fork</em> de este repositorio y clónalo en tu equipo.</li>
  <li>Usa un <strong>&lt;ALIAS&gt;</strong> sin espacios ni acentos: tu usuario de GitHub (recomendado) o <code>nombre-apellido</code> todo en minúsculas. Ej.: <code>juana-saavedra</code> o <code>juana</code>.</li>
  <li>Para <strong>cada mini-reto</strong>, crea un archivo con <strong>este nombre exacto</strong>:
    <br><code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code>
    <br>Ej.: <code>1005_juana-saavedra_v1.py</code>, <code>1007_juana_v2.py</code>.
  </li>
  <li>Si construyes la <strong>app integrada (código 1900)</strong>, crea la carpeta:
    <br><code>1900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code>, (opcional) <code>requirements.txt</code> y la carpeta <code>src/</code>.
  </li>
  <li>Cuando termines, sube tus cambios a tu fork y abre un Pull Request hacia <code>main</code> con título: <strong>&lt;ALIAS&gt; — Entrega Nivel Básico</strong>.</li>
</ol>

<hr />

<h2>Por qué nuestros mini-retos “básicos” no son tan cortos</h2>
<p>
  En la vida real programar no es adivinar, es <strong>leer documentación</strong>, <strong>entender especificaciones</strong>, y <strong>cuidar detalles</strong>. Por eso los enunciados piden cosas muy concretas: normalizar acentos, redondear con una regla específica, leer varias líneas hasta EOF, respetar una semilla para que los resultados sean reproducibles, etc.  
  Una IA que no “lee” docs suele fallar en esos detalles; si tú sí las lees, lo vas a sacar sin problema. Este es el aprendizaje que buscamos.
</p>

<hr />

<h2>Convención de códigos (Nivel Básico)</h2>
<ul>
  <li><strong>Mini-retos:</strong> del <code>1001</code> al <code>1008</code> (elige y completa 7 u 8).</li>
  <li><strong>App integrada:</strong> <code>1900</code> (<em>Math &amp; Logic Kit</em>) — debe reutilizar tus mini-retos.</li>
</ul>
<p><strong>Nombre de archivo obligatorio:</strong> <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code> · Ej.: <code>1007_juana_v1.py</code></p>

<hr />

<h2>Mini-retos (ideas, requisitos y documentación)</h2>
<p>
  Entrega <strong>7 u 8</strong> en 3 horas. Todos con <strong>librería estándar</strong> de Python.  
  Al final de cada archivo, agrega en comentarios <strong>3 casos de prueba</strong> (entrada → salida esperada), por ejemplo:
</p>
<pre><code># PRUEBAS
# in: 5.005 + 2
# out: 7.01
# in: 10 / 0
# out: ERROR:DIV0
# in: 1.005 * 3
# out: 3.02
</code></pre>

<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Nombre</th>
      <th>Qué se espera (con detalles “anti-IA”)</th>
      <th>Entrada / Salida mínima</th>
      <th>Archivo</th>
      <th>Docs útiles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1001</strong></td>
      <td>Calculadora precisa</td>
      <td>
        Implementa + − × ÷ usando <strong>redondeo comercial</strong> a 2 decimales (no “ties to even”). Debes usar <code>decimal.Decimal</code> con <code>ROUND_HALF_UP</code>.
        Si hay división por cero, imprime exactamente <code>ERROR:DIV0</code>.  
        <em>Anti-IA:</em> muchas soluciones con IA se quedan en <code>round()</code> (banco) y fallan en los casos límite.
      </td>
      <td>Entrada: <code>a op b</code> (ej. <code>5.005 + 2</code>) · Salida: número a 2 decimales.</td>
      <td><code>1001_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/decimal.html" target="_blank">decimal</a></td>
    </tr>

    <tr>
      <td><strong>1002</strong></td>
      <td>Ecuación de 2º grado</td>
      <td>
        Resuelve <code>ax^2 + bx + c = 0</code>. Reglas:
        <ul>
          <li>Si <code>a=0</code>, trátalo como ecuación lineal.</li>
          <li>Imprime <code>delta=...</code> y:
            <ul>
              <li>Si Δ &gt;= 0 y es <em>cuadrado perfecto</em>, raíces <strong>enteras exactas</strong>.</li>
              <li>Si Δ &gt; 0 y no es perfecto, usa <code>Decimal</code> a 4 decimales (ROUND_HALF_UP).</li>
              <li>Si Δ &lt; 0, imprime <code>sin raices reales</code>.</li>
            </ul>
          </li>
        </ul>
        <em>Anti-IA:</em> no olvidar el caso <code>a=0</code> ni distinguir Δ perfecto.
      </td>
      <td>Entrada: <code>a b c</code> · Salida: <code>delta=... r1=... r2=...</code> o <code>sin raices reales</code>.</td>
      <td><code>1002_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/math.html" target="_blank">math</a> · <a href="https://docs.python.org/3/library/decimal.html" target="_blank">decimal</a></td>
    </tr>

    <tr>
      <td><strong>1003</strong></td>
      <td>Adivina el número (semilla)</td>
      <td>
        Juego 1..100 con pistas ↑/↓ y conteo de intentos. Debe aceptar <code>--seed=&lt;n&gt;</code> y usar <code>random.seed()</code> para que el número sea reproducible.  
        <em>Anti-IA:</em> si no respeta la semilla, los tests no coinciden.
      </td>
      <td>I/O en consola; termina con “<code>acertaste en N</code>”.</td>
      <td><code>1003_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/random.html" target="_blank">random</a> · <a href="https://docs.python.org/3/library/argparse.html" target="_blank">argparse</a> (opcional)</td>
    </tr>

    <tr>
      <td><strong>1004</strong></td>
      <td>Conversor °C↔°F↔K (múltiples líneas)</td>
      <td>
        Lee <strong>varias líneas</strong> desde stdin (hasta EOF). Soporta unidades <code>C</code>, <code>F</code>, <code>K</code>.  
        Si el resultado es &lt; 0 K, imprime <code>ERROR:ABSOLUTE_ZERO</code>. Redondea a 2 decimales con <code>Decimal</code>.  
        <em>Anti-IA:</em> fallan si no leen hasta EOF o si no controlan 0 K.
      </td>
      <td>Cada línea: <code>valor unidad_origen unidad_destino</code> · Salida: una línea por conversión.</td>
      <td><code>1004_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/tutorial/inputoutput.html" target="_blank">I/O</a> · <a href="https://docs.python.org/3/library/decimal.html" target="_blank">decimal</a></td>
    </tr>

    <tr>
      <td><strong>1005</strong></td>
      <td>¿Es primo? (hasta 10<sup>6</sup>)</td>
      <td>
        Imprime <code>primo</code> o <code>no primo</code> para <code>n</code>. Por definición, 0, 1 y negativos → <code>no primo</code>.  
        Optimiza parando los intentos en <code>√n</code>.  
        <em>Anti-IA:</em> a veces hacen bucles innecesarios o fallan con casos pequeños.
      </td>
      <td>Entrada: <code>n</code> · Salida: <code>primo</code> / <code>no primo</code>.</td>
      <td><code>1005_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/math.html" target="_blank">math</a></td>
    </tr>

    <tr>
      <td><strong>1006</strong></td>
      <td>Tabla de multiplicar “bonita”</td>
      <td>
        Imprime la tabla de <code>N</code> del 1 al 10, alineada en columnas, sin espacios extra al final de línea.  
        <em>Anti-IA:</em> muchas respuestas descuidan espacios/saltos; aquí la comparación es literal.
      </td>
      <td>Entrada: <code>N</code> · Salida: 10 líneas “<code>N x i = r</code>” alineadas.</td>
      <td><code>1006_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/string.html#format-string-syntax" target="_blank">format strings</a></td>
    </tr>

    <tr>
      <td><strong>1007</strong></td>
      <td>Palíndromos con acentos y signos</td>
      <td>
        Detecta palíndromos ignorando mayúsculas/minúsculas, espacios, puntuación y <strong>acentos/diacríticos</strong>.  
        Normaliza con <code>unicodedata</code> (NFKD) y filtra las marcas de combinación.  
        <em>Anti-IA:</em> soluciones “rápidas” fallan con tildes, ñ o emojis.
      </td>
      <td>Entrada: línea de texto · Salida: <code>si</code> / <code>no</code>.</td>
      <td><code>1007_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/unicodedata.html" target="_blank">unicodedata</a></td>
    </tr>

    <tr>
      <td><strong>1008</strong></td>
      <td>Simulador de dados (histograma)</td>
      <td>
        Simula <code>N</code> lanzamientos y muestra frecuencias para 1..6 en orden.  
        Acepta <code>--seed</code> para reproducibilidad.  
        <em>Anti-IA:</em> sin semilla, las salidas no coinciden con pruebas.
      </td>
      <td>Entrada: <code>N</code> (y opcional <code>--seed</code>) · Salida: 6 líneas “<code>cara: conteo</code>”.</td>
      <td><code>1008_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/random.html" target="_blank">random</a> · <a href="https://docs.python.org/3/library/argparse.html" target="_blank">argparse</a></td>
    </tr>
  </tbody>
</table>

<h3>Requisitos mínimos por mini-reto</h3>
<ul>
  <li><strong>I/O exacta</strong>: los tests comparan texto literal (ojo con mayúsculas, espacios y saltos de línea).</li>
  <li><strong>3 casos de prueba</strong> en comentarios al final del archivo (entrada → salida esperada).</li>
  <li><strong>Solo librería estándar</strong> de Python.</li>
  <li><strong>Nombre de archivo exacto</strong> (formato indicado). Nombre incorrecto = −5%.</li>
</ul>

<hr />

<h2>App integrada del nivel básico</h2>
<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Nombre</th>
      <th>Debe reutilizar</th>
      <th>Qué agrega</th>
      <th>Entregables</th>
      <th>Puntaje máx.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1900</strong></td>
      <td>Math &amp; Logic Kit</td>
      <td>Tu propia lógica de: 1001, 1002, 1003, 1005, 1006, 1007, 1008</td>
      <td>Un <strong>menú en consola</strong> que ejecute tus funciones, manejo básico de errores y mensajes claros.</td>
      <td>Carpeta <code>1900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo correr y qué módulos integra) y <code>src/</code>.</td>
      <td><strong>140</strong></td>
    </tr>
  </tbody>
</table>

<h3>Tips para la app</h3>
<ul>
  <li>No reescribas: <strong>importa</strong> tus funciones desde los mini-retos o muévelas a <code>src/utils.py</code> y reúsalas.</li>
  <li>Menú simple (opciones 1..7 + salir). Mantén mensajes consistentes y amables.</li>
  <li>Si algo falla, muestra un mensaje breve (no un traceback completo).</li>
</ul>

<hr />

<h2>Puntajes — Nivel Básico</h2>
<ul>
  <li><strong>Mini-reto:</strong> hasta <strong>70 pts</strong> c/u
    <ul>
      <li>Funciona (casos base): 60%</li>
      <li>Casos borde / 3 pruebas documentadas: 20%</li>
      <li>Código claro (nombres, comentarios mínimos): 10%</li>
      <li>Defensa breve (2–3 min): 10%</li>
    </ul>
  </li>
  <li><strong>App 1900:</strong> hasta <strong>140 pts</strong>
    <ul>
      <li>Integra y navega por los mini-retos: 50%</li>
      <li>Cohesión (reuso de funciones/utilidades): 20%</li>
      <li>Manejo de errores básico: 20%</li>
      <li>README con instrucciones: 10%</li>
    </ul>
  </li>
</ul>

<hr />

<h2>Prevención de uso de IA: desde la consigna</h2>
<p>
  Los retos fuerzan a que la salida sea <strong>exacta</strong> y a que uses módulos concretos de la librería estándar.  
  Esto obliga a <strong>leer documentación</strong> y evita soluciones “adivinadas”.
</p>
<ul>
  <li><strong>Redondeo con <code>decimal</code></strong> y <code>ROUND_HALF_UP</code> (1001, 1002, 1004).</li>
  <li><strong>Semillas reproducibles</strong> y argumentos de línea (1003, 1008).</li>
  <li><strong>Normalización Unicode</strong> (1007) para acentos/diacríticos.</li>
  <li><strong>Lectura múltiple hasta EOF</strong> (1004) y <strong>formato exacto</strong> (1006).</li>
</ul>
<p>
  Durante la revisión, podemos pedir una <strong>edición en vivo de 2 minutos</strong> (por ejemplo, cambiar un formato o agregar un caso borde).  
  Si escribiste y entendiste tu código, esto será fácil.
</p>

<hr />

<h2>Checklist final</h2>
<ul>
  <li>✔ 7 u 8 mini-retos con nombres correctos: <code>100x_&lt;ALIAS&gt;_vN.py</code></li>
  <li>✔ Cada archivo incluye 3 pruebas (en comentarios)</li>
  <li>✔ Si hiciste la app: carpeta <code>1900_&lt;ALIAS&gt;_app/</code> + <code>README.md</code> + menú funcional</li>
  <li>✔ Pull Request con título <code>&lt;ALIAS&gt; — Entrega Nivel Básico</code> y breve descripción</li>
</ul>

<h2>Documentación recomendada de Python</h2>
<p>
  <a href="https://docs.python.org/3/" target="_blank">Guía oficial</a> ·
  <a href="https://docs.python.org/3/library/decimal.html" target="_blank">decimal</a> ·
  <a href="https://docs.python.org/3/library/random.html" target="_blank">random</a> ·
  <a href="https://docs.python.org/3/library/argparse.html" target="_blank">argparse</a> ·
  <a href="https://docs.python.org/3/library/unicodedata.html" target="_blank">unicodedata</a> ·
  <a href="https://docs.python.org/3/tutorial/inputoutput.html" target="_blank">I/O</a> ·
  <a href="https://docs.python.org/3/library/string.html#format-string-syntax" target="_blank">format strings</a>
</p>

<h2>Dudas</h2>
<p>Abre un Issue titulado <code>Q-&lt;ALIAS&gt;: asunto</code>. ¡Éxitos y a programar! 🚀</p>
