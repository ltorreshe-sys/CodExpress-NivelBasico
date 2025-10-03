<h1>CodExpress — Nivel Básico (Fundamentos y Lógica)</h1>
<p>⏱️ <strong>Tiempo total:</strong> 3 horas · <strong>Meta:</strong> completar 7–8 mini-retos y (opcional) 1 app integrada usando esos mini-retos.</p>

<h2>Cómo participar (fork &amp; PR)</h2>
<ol>
  <li>Haz <em>fork</em> de este repositorio y clónalo en tu equipo.</li>
  <li>Crea una rama con tu TeamID numérico: <code>equipo-####</code> (ej.: <code>equipo-0042</code>).</li>
  <li>Por cada mini-reto, entrega un archivo con <strong>nomenclatura obligatoria</strong>:
    <br><code>&lt;CODIGO_RETO&gt;_&lt;TEAMID&gt;_&lt;INICIALES&gt;_v&lt;N&gt;.&lt;ext&gt;</code>
    <br>Ej.: <code>1005_0042_JSS_v1.py</code>
  </li>
  <li>Para la app integrada (código <strong>1900</strong>) crea una carpeta:
    <br><code>1900_&lt;TEAMID&gt;_app/</code> con <code>README.md</code>, <code>requirements.txt</code> (si aplica) y <code>src/</code>.
  </li>
  <li>Abre un Pull Request a <code>main</code> titulado: <strong>TEAM #### – Entrega Nivel Básico</strong>.</li>
</ol>

<hr>

<h2>Convención de códigos (sin letras)</h2>
<ul>
  <li><strong>Mini-retos:</strong> 1001–1008</li>
  <li><strong>App integrada:</strong> 1900 (debe usar mini-retos del 1001 al 1008 según se indica abajo)</li>
</ul>
<p><strong>Nombre de archivo obligatorio:</strong> <code>&lt;CODIGO_RETO&gt;_&lt;TEAMID&gt;_&lt;INICIALES&gt;_v&lt;N&gt;.&lt;ext&gt;</code> · TeamID numérico (3–4 dígitos) · INICIALES (2–4 letras, ej.: JSS, ALP).</p>

<h2>Estructura sugerida del repo</h2>
<pre>
.
├── 1001_0042_JSS_v1.py
├── 1002_0042_ALP_v1.py
├── ...
├── 1008_0042_MRG_v1.py
└── 1900_0042_app/
    ├── README.md
    ├── requirements.txt
    └── src/
</pre>

<hr>

<h2>Tabla · Mini-retos (ideas, requisitos y documentación)</h2>
<p>Entrega <strong>7–8 mini-retos</strong> dentro de las 3 horas. Usa el nombre de archivo indicado en cada fila.</p>

<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Nombre</th>
      <th>Descripción</th>
      <th>Entrada/Salida mínima</th>
      <th>Archivo esperado</th>
      <th>Docs útiles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1001</strong></td>
      <td>Calculadora básica</td>
      <td>Suma, resta, multiplicación, división. Validar división por cero.</td>
      <td>Entrada: <code>a op b</code> (ej.: <code>5 * 7</code>). Salida: resultado en una línea.</td>
      <td><code>1001_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/tutorial/">Python</a> · <a href="https://en.cppreference.com/w/">C++</a> · <a href="https://docs.oracle.com/javase/tutorial/">Java</a></td>
    </tr>
    <tr>
      <td><strong>1002</strong></td>
      <td>Ecuación de 2º grado</td>
      <td>Resolver ax²+bx+c (mostrar Δ y raíces reales o mensaje si no hay reales).</td>
      <td>Entrada: <code>a b c</code>. Salida: <code>delta=... r1=... r2=...</code> o “sin raíces reales”.</td>
      <td><code>1002_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/math.html">math</a></td>
    </tr>
    <tr>
      <td><strong>1003</strong></td>
      <td>Adivina el número</td>
      <td>Número aleatorio 1..100; dar pistas ↑/↓ y contar intentos.</td>
      <td>I/O libre en consola; imprimir “mayor/menor/acertaste en N intentos”.</td>
      <td><code>1003_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/random.html">random</a></td>
    </tr>
    <tr>
      <td><strong>1004</strong></td>
      <td>Conversor °C↔°F</td>
      <td>Convertir temperaturas con formato claro y redondeo a 2 decimales.</td>
      <td>Entrada: <code>valor unidad_origen unidad_destino</code> (ej.: <code>100 C F</code>). Salida: número.</td>
      <td><code>1004_TEAM_INI_v1.py</code></td>
      <td><a href="https://developer.mozilla.org/docs/Web/JavaScript">MDN JS</a></td>
    </tr>
    <tr>
      <td><strong>1005</strong></td>
      <td>¿Es primo?</td>
      <td>Prueba de primalidad simple (opcional optimización hasta √n).</td>
      <td>Entrada: <code>n</code>. Salida: “primo” o “no primo”.</td>
      <td><code>1005_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/tutorial/controlflow.html">control flow</a></td>
    </tr>
    <tr>
      <td><strong>1006</strong></td>
      <td>Tabla de multiplicar</td>
      <td>Imprimir tabla del número N del 1 al 10 con formato alineado.</td>
      <td>Entrada: <code>n</code>. Salida: 10 líneas con “n x i = r”.</td>
      <td><code>1006_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/tutorial/introduction.html">basics</a></td>
    </tr>
    <tr>
      <td><strong>1007</strong></td>
      <td>Palíndromos</td>
      <td>Detectar si una cadena es palíndromo ignorando espacios/acentos.</td>
      <td>Entrada: línea de texto. Salida: “si” o “no”.</td>
      <td><code>1007_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/stdtypes.html#textseq">strings</a></td>
    </tr>
    <tr>
      <td><strong>1008</strong></td>
      <td>Simulador de dados</td>
      <td>Simular N lanzamientos (1..6) y mostrar frecuencias.</td>
      <td>Entrada: <code>N</code>. Salida: 6 líneas “valor: conteo”.</td>
      <td><code>1008_TEAM_INI_v1.py</code></td>
      <td><a href="https://docs.python.org/3/library/random.html">random</a></td>
    </tr>
  </tbody>
</table>

<h3>Requisitos mínimos por mini-reto</h3>
<ul>
  <li><strong>I/O limpia</strong> en consola (sin menús extensos).</li>
  <li><strong>3 casos de prueba</strong> en comentarios al final del archivo (entrada → salida esperada).</li>
  <li><strong>Sin dependencias externas</strong> obligatorias (solo librerías estándar).</li>
  <li><strong>Nomenclatura de archivo</strong> exacta (ver arriba). Entregas con nombre diferente: −5%.</li>
</ul>

<hr>

<h2>App integrada del nivel básico</h2>
<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Nombre</th>
      <th>Mini-retos requeridos</th>
      <th>Requisitos extra</th>
      <th>Entregables</th>
      <th>Puntaje máx.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1900</strong></td>
      <td>Math &amp; Logic Kit</td>
      <td>Usar y enlazar funcionalmente: 1001, 1002, 1003, 1005, 1006, 1007, 1008</td>
      <td>Menú simple en consola, validación de entradas, manejo básico de errores.</td>
      <td>Carpeta <code>1900_TEAM_app/</code> con <code>README.md</code> (instrucciones y qué mini-retos usa) y <code>src/</code>.</td>
      <td><strong>140</strong></td>
    </tr>
  </tbody>
</table>

<h3>Notas sobre la app</h3>
<ul>
  <li>La app <strong>debe reutilizar</strong> el código o lógica de los mini-retos (no reescribir todo desde cero).</li>
  <li>Menú en consola que permita ejecutar cada módulo (p. ej., “1) Calculadora, 2) Primos, ...”).</li>
  <li>Si comparten utilidades (p. ej., validación), colócalas en <code>src/utils.py</code> o similar.</li>
</ul>

<hr>

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
  <li><strong>App integrada (1900):</strong> hasta <strong>140 pts</strong>
    <ul>
      <li>Integra y navega por los mini-retos requeridos: 50%</li>
      <li>Cohesión (reuso de funciones/utilidades): 20%</li>
      <li>Manejo de errores básico: 20%</li>
      <li>README con instrucciones: 10%</li>
    </ul>
  </li>
</ul>

<hr>

<h2>Rúbrica Anti-IA (Nivel Básico)</h2>
<p>Usar IA como apoyo está permitido; <strong>ganar</strong> requiere demostrar autoría y comprensión.</p>
<ul>
  <li><strong>Defensa y edición en vivo</strong> (hasta 10% del reto): el jurado pedirá un cambio simple (ej.: añadir chequeo de entrada vacía o cambiar el formato de salida). Debe implementarse en minutos y explicarse.</li>
  <li><strong>Coherencia de estilo</strong> (5%): nombres y comentarios consistentes entre archivos del equipo.</li>
  <li><strong>Señales de I
