¡buenísimo, lo hacemos **solo para el Nivel Básico** y sin TeamID!
Aquí tienes el **README en HTML compatible con GitHub** (sin CSS/JS en `<head>`). Está escrito para que cualquiera lo lea con calma, entienda el “por qué” de cada cosa y, además, incorpora **prevención de uso de IA desde el diseño de los retos** (pedimos cosas que los modelos suelen fallar si no leen la documentación de Python).

> **Cómo nombrar tus archivos:** usa tu **usuario de GitHub** (recomendado) o tu **nombre-apellido** en minúsculas y sin espacios/acentos. A esto le llamaremos `<ALIAS>`.
> Formato obligatorio:
> `&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;`
> Ejemplos: `1005_juanasaavedra_v1.py`, `1007_jsaavedra_v2.py`

---

```html
<h1>CodExpress — Nivel Básico (Fundamentos y Lógica)</h1>
<p><strong>Tiempo total:</strong> 3 horas · <strong>Objetivo:</strong> completar <u>7 u 8 mini-retos</u> y, si alcanzas, una <u>app integrada (1900)</u> que reutilice tu propio código.</p>

<h2>¿Cómo trabajamos en este repo?</h2>
<ol>
  <li>Haz <em>fork</em> de este repositorio y clónalo en tu compu.</li>
  <li>Trabaja con tu propio <strong>&lt;ALIAS&gt;</strong> (tu usuario de GitHub o nombre-apellido en minúsculas, sin espacios/acentos).</li>
  <li>Por cada mini-reto, crea un archivo con <strong>este nombre exacto</strong>:
    <br><code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code>
    <br>Ej.: <code>1005_jsaavedra_v1.py</code>
  </li>
  <li>Si construyes la app integrada (código <strong>1900</strong>), crea:
    <br><code>1900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code>, (opcional) <code>requirements.txt</code> y carpeta <code>src/</code>.</li>
  <li>Cuando termines, sube tus cambios en tu fork y abre un Pull Request hacia <code>main</code> con título: <strong>&lt;ALIAS&gt; — Entrega Nivel Básico</strong>.</li>
</ol>

<hr>

<h2>Por qué nuestros mini-retos “básicos” no son tan cortos</h2>
<p>Queremos que aprendas a <strong>leer documentación</strong>, a <strong>entender especificaciones</strong> y a <strong>cuidar detalles</strong>. Por eso los enunciados piden cosas concretas (p. ej., normalizar acentos, redondear con reglas específicas, leer varias líneas de entrada). Esto es clave en programación real.</p>
<p>Además, los retos están diseñados para que una IA que “adivina” sin leer docs tiende a fallar. Si tú lees la documentación (enlaces incluidos) y entiendes lo que haces, vas a poder completarlos sin problema.</p>

<hr>

<h2>Convención de códigos (Nivel Básico)</h2>
<ul>
  <li><strong>Mini-retos:</strong> 1001–1008 (elige y completa 7 u 8)</li>
  <li><strong>App integrada:</strong> 1900 (<em>Math &amp; Logic Kit</em>) — reutiliza tus propios mini-retos</li>
</ul>
<p><strong>Nombre de archivo obligatorio:</strong> <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code> · Ej.: <code>1007_jsaavedra_v1.py</code></p>

<hr>

<h2>Mini-retos (ideas, requisitos y documentación)</h2>
<p>Entrega <strong>7 u 8</strong> en 3 horas. Cada archivo debe incluir al final, en comentarios, <strong>3 casos de prueba</strong> (entrada → salida esperada). Los retos usan solo librería estándar.</p>

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
        Operaciones + − × ÷ con <u>redondeo comercial</u> a 2 decimales (no el redondeo “bancario” por defecto de <code>round()</code>). 
        Debes usar <code>decimal.Decimal</code> con <code>ROUND_HALF_UP</code>. Si hay división por cero: imprimir exactamente <code>ERROR:DIV0</code>.
        <br><em>Anti-IA:</em> muchos modelos olvidan que <code>round()</code> en Python usa “ties to even”. Aquí pedimos explícitamente otra regla.
      </td>
      <td>Entrada: <code>a op b</code> (ej. <code>5.005 + 2</code>) · Salida: número con 2 decimales.</td>
      <td><code>1001_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/decimal.html">decimal</a></td>
    </tr>

    <tr>
      <td><strong>1002</strong></td>
      <td>Ecuación de 2º grado</td>
      <td>
        Resolver <code>ax^2 + bx + c = 0</code>. Imprime Δ, y:
        <ul>
          <li>Si <code>a=0</code>, resolver como <em>ecuación lineal</em>.</li>
          <li>Si Δ &gt;= 0 y es <em>cuadrado perfecto</em>, imprime raíces exactas como enteros.</li>
          <li>Si Δ &gt; 0 y no es perfecto, imprime con <code>Decimal</code> a 4 decimales (ROUND_HALF_UP).</li>
          <li>Si Δ &lt; 0, imprimir <code>sin raices reales</code>.</li>
        </ul>
        <em>Anti-IA:</em> muchos modelos omiten el caso <code>a=0</code> o no distinguen Δ perfecto.
      </td>
      <td>Entrada: <code>a b c</code> · Salida: <code>delta=... r1=... r2=...</code> o <code>sin raices reales</code>.</td>
      <td><code>1002_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/math.html">math</a> · <a href="https://docs.python.org/3/library/decimal.html">decimal</a></td>
    </tr>

    <tr>
      <td><strong>1003</strong></td>
      <td>Adivina el número (semilla)</td>
      <td>
        Juego 1..100 con pistas ↑/↓ y conteo de intentos. Debe aceptar <code>--seed=&lt;n&gt;</code> para que el número sea reproducible (usar <code>random.seed()</code>). 
        <br><em>Anti-IA:</em> si no respeta la semilla, los tests no coinciden.
      </td>
      <td>I/O libre en consola; terminar con “<code>acertaste en N</code>”.</td>
      <td><code>1003_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/random.html">random</a> · <a href="https://docs.python.org/3/library/argparse.html">argparse</a> (opcional)</td>
    </tr>

    <tr>
      <td><strong>1004</strong></td>
      <td>Conversor °C↔°F↔K (múltiples líneas)</td>
      <td>
        Convierte varias líneas desde <em>stdin</em> (hasta EOF). Soporta <code>C</code>, <code>F</code>, <code>K</code>. Si el resultado es &lt; 0 K: imprimir <code>ERROR:ABSOLUTE_ZERO</code>. 
        Redondeo a 2 decimales con <code>Decimal</code>.
        <br><em>Anti-IA:</em> suele olvidar leer múltiples líneas o el cero absoluto.
      </td>
      <td>Cada línea: <code>valor unidad_origen unidad_destino</code> · Salida: una línea por conversión.</td>
      <td><code>1004_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/tutorial/inputoutput.html">I/O</a> · <a href="https://docs.python.org/3/library/decimal.html">decimal</a></td>
    </tr>

    <tr>
      <td><strong>1005</strong></td>
      <td>¿Es primo? (hasta 10<sup>6</sup>)</td>
      <td>
        Imprime <code>primo</code> o <code>no primo</code> para <code>n</code> (0, 1 y negativos son <code>no primo</code>). 
        Debe detener divisiones en <code>√n</code>. 
        <br><em>Anti-IA:</em> muchas soluciones hacen bucles ineficientes o fallan con n pequeños.
      </td>
      <td>Entrada: <code>n</code> · Salida: <code>primo</code> / <code>no primo</code>.</td>
      <td><code>1005_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/tutorial/controlflow.html">control flow</a> · <a href="https://docs.python.org/3/library/math.html">math</a></td>
    </tr>

    <tr>
      <td><strong>1006</strong></td>
      <td>Tabla de multiplicar “bonita”</td>
      <td>
        Imprime la tabla de <code>N</code> del 1 al 10 alineada en columnas, sin espacios al final de la línea. 
        <br><em>Anti-IA:</em> se penaliza dejar espacios/formatos inconsistentes (los tests comparan exacto).
      </td>
      <td>Entrada: <code>N</code> · Salida: 10 líneas “<code>N x i = r</code>” alineadas.</td>
      <td><code>1006_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/string.html#format-string-syntax">format</a></td>
    </tr>

    <tr>
      <td><strong>1007</strong></td>
      <td>Palíndromos con acentos y signos</td>
      <td>
        Detectar palíndromos ignorando mayúsculas/minúsculas, espacios, signos y <u>acentos/diacríticos</u>. 
        Debes normalizar con <code>unicodedata</code> (NFKD) y filtrar combinaciones.
        <br><em>Anti-IA:</em> soluciones “rápidas” fallan en cadenas con tildes/ñ/emoji.
      </td>
      <td>Entrada: línea de texto · Salida: <code>si</code> / <code>no</code>.</td>
      <td><code>1007_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/unicodedata.html">unicodedata</a></td>
    </tr>

    <tr>
      <td><strong>1008</strong></td>
      <td>Simulador de dados (histograma)</td>
      <td>
        Recibe <code>N</code> lanzamientos y genera frecuencias de 1..6. Si se pasa <code>--seed</code>, el resultado debe ser reproducible. 
        Ordena la salida por cara (1→6).
        <br><em>Anti-IA:</em> sin semilla no habrá coincidencia con tests.
      </td>
      <td>Entrada: <code>N</code> (y opcional <code>--seed</code>) · Salida: 6 líneas “<code>cara: conteo</code>”.</td>
      <td><code>1008_&lt;ALIAS&gt;_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/random.html">random</a> · <a href="https://docs.python.org/3/library/argparse.html">argparse</a></td>
    </tr>
  </tbody>
</table>

<h3>Requisitos mínimos por mini-reto</h3>
<ul>
  <li><strong>I/O exacta</strong>: los tests comparan texto literal (cuidado con mayúsculas, espacios y saltos de línea).</li>
  <li><strong>3 casos de prueba</strong> como comentarios al final del archivo (entrada → salida esperada).</li>
  <li><strong>Sin librerías externas</strong>; solo estándar de Python.</li>
  <li><strong>Nombre de archivo exacto</strong> (formato indicado). Nombre incorrecto = −5%.</li>
</ul>

<hr>

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
      <td>1001, 1002, 1003, 1005, 1006, 1007, 1008 (módulos propios)</td>
      <td>Un <strong>menú en consola</strong> que llame a tus funciones, manejo básico de errores y mensajes claros.</td>
      <td>Carpeta <code>1900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo correr, qué módulos integra) y <code>src/</code>.</td>
      <td><strong>140</strong></td>
    </tr>
  </tbody>
</table>

<h3>Tips para la app</h3>
<ul>
  <li>No reescribas: <strong>importa</strong> tus funciones desde los archivos de mini-retos o muévelas a un módulo común (<code>src/utils.py</code>) y reúsalas.</li>
  <li>Mantén el menú simple: números del 1 al 7; una opción para salir.</li>
  <li>Si algo falla, explica en una línea qué pasó (sin trazar todo el error).</li>
</ul>

<hr>

<h2>Puntajes — Nivel Básico</h2>
<ul>
  <li><strong>Mini-reto:</strong> hasta <strong>70 pts</strong>
    <ul>
      <li>Funciona (casos base): 60%</li>
      <li>Casos borde / 3 pruebas documentadas: 20%</li>
      <li>Código claro (nombres, comentarios mínimos): 10%</li>
      <li>Defensa breve (2–3 min): 10%</li>
    </ul>
  </li>
  <li><strong>App 1900:</strong> hasta <strong>140 pts</strong>
    <ul>
      <li>Integra y navega por los mini-retos requeridos: 50%</li>
      <li>Cohesión (reuso de funciones/utilidades): 20%</li>
      <li>Manejo de errores básico: 20%</li>
      <li>README con instrucciones: 10%</li>
    </ul>
  </li>
</ul>

<hr>

<h2>Prevención de uso de IA: desde la consigna</h2>
<p>Hemos diseñado los retos para que la salida <strong>deba coincidir exactamente</strong>, para que se usen módulos concretos de la librería estándar y para que se atiendan casos borde. Estos son puntos donde los modelos suelen fallar si no “leen”:</p>
<ul>
  <li><strong>Reglas de redondeo específicas</strong> con <code>decimal</code> (1001, 1002, 1004).</li>
  <li><strong>Semillas reproducibles</strong> y argumentos de línea de comandos (1003, 1008).</li>
  <li><strong>Normalización Unicode</strong> de acentos y signos (1007).</li>
  <li><strong>Lectura múltiple hasta EOF</strong> (1004) y <strong>formato exacto</strong> (1006).</li>
</ul>
<p>Además, durante la revisión podemos pedir una <strong>edición en vivo de 2 minutos</strong> (p. ej., cambiar el símbolo de salida, agregar un caso borde). Si dominas tu código, lo harás sin problema.</p>

<hr>

<h2>Checklist final</h2>
<ul>
  <li>✔ 7 u 8 mini-retos con nombre exacto: <code>100x_&lt;ALIAS&gt;_vN.py</code></li>
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
```
