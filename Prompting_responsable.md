# Prompting responsable: maximiza la IA en tu negocio

## 1. Prompt engineering - La IA como nuestro "copiloto"
* Cuando hablamos de *Prompt engineering* nos referimos a la forma en que relacionamos y específicamente a la forma como le hablamos y le preguntamos cosas a la IA.
***

## 2. Prompt engineering - Un día con IA
+ Integrar la IA en las actividades cotidianas que tenemos (ayuda a facilitar tareas en donde tardaríamos algunas horas.)
+ Puede ayudarnos a la elección de menú para cuidarnos en cuestión de alergias.
+ Nos permite crear *apps webs* para que podamos practicar habilidades, tales como las tablas de multiplicar.
+ Se hace mucho más durante el día pues la combinación de *piloto + copiloto*.
***

## 3. Prompt engineering - Estructura de los prompts
+ La calidad de las respuestas que obtenemos dependen en gran medida de cómo formulamos nuestras preguntas y del contexto que le proporcionamos .
+ El *prompting* es, en esencia el arte de guiar al modelo para que nos dé la mejor respuesta posible. Y la clave para que esto funciones bien es ofrecer un buen contexto.
+ Los modelos de lenguaje no razonan como los humanos, pero son increíblemente buenos a la hora de identificar patrones y relaciones entre palabras en los datos con los que han sido entrenados.
+ Sí se le proporciona al modelo de IA un contexto claro, como indicarle el público al que va dirigida la explicación, o el tipo de tono que se prefiere la respuesta va a ser mucho más ajustada a las necesidades establecidas.
+ La diferencia en la calidad de las respuestas recae en el prompt.

#### Estructura de los prompts
1. Objetivo 
>¿Qué necesitas que haga: resumir, traducir, ordenar, generar un post, una carta, una poesía...?
2. Contexto
>¿Por qué lo necesitas? ¿A quién impacta? ¿Qué intentas conseguir?
3. Expectativas
>¿Cómo debería responder la IA para cumplir con tu petición? A nivel de formato, de tono, de origen de la información...

Lo principal es que el objetivo sea claro y directo. Así como los dos pasos restantes de la lista. Si no lo hacemos, la inteligencia artificial lo hará por ti y puede que la respuesta no sea exactamente la que se necesite.
+ El primer resultado no necesariamente es la respuesta final y es normal, pues se entra en un dialogo continuo.
+ Si la respuesta no es aceptable, podemos pedir que la modifique, que añada, que elimine partes, que modifique algo del contenido.

***

## 4. Prompt engineering - Técnicas y prácticas I
#### Ve al grano y sin protocolos.
>Con la IA no hace falta ser especialmente educado ni refinado, así que no hace falta que se incluyan palabras como *por favor*, ni me *gustaría*. Las ordenes directas y sencillas darán muchos mejores resultados.

En lugar de *¿Podrías explicarme, por favor, la estructura de una célula humana?*, pídele *Explica la estructura de una célula humana.*

O bien, en lugar de *Me preguntaba si podrías, por favor, darme  algunas sugerencias sobre cómo mejorar mi productividad en el trabajo.* Di *Dame sugerencias para mejorar mi productividad en el trabajo.*

¿Por qué?
Cuando se escribe un prompt que incluye frases como *por favor, me gustaría, podrías* se está añadiendo información que es completamente irrelevante para el modelo, es decir, pueden añadir ruido al prompt, incluso puede hacer que la IA gaste recursos procesando partes del mensaje que en realidad no son importantes.

#### Usa delimitaodores en tus prompts
Podemos escoger símbolos que representen saltos de línea para mantener una estructura clara la cual permita que se entiendan nuestras instrucciones sin ambigüedad. Tanto como comillas, barras, etc., sirven como delimitadores. Un caso sería la sintaxis de LaTeX.

En lugar de
>*Traduce esto al inglés. Hola, ¿cómo estás? Me gustaría jugar en el parque. Mi color favorito es el azul. Esta traducción es para una clase de inglés para niños de primaría. Usa vocabulario sencillo y frases cortas.*

decir
>Traduce esto al inglés:
<br> // <br>
Hola, ¿cómo estás? <br>
Me gusta jugar en el parque. <br>
Mi color favorito es el azul. <br>
// <br>
Esta traducción es para una clase de inglés para niños de primaria. Usa vocabulario sencillo y frases cortas.


Otro ejemplo correcto
>Analiza las siguientes estadísticas y proporciona insights: <br>
-- <br>
Tasa de desempleo 2020: 8.9% <br>
Tasa de desempleo 2021: 7.8% <br>
Tasa de desempleo 2022: 6.3% <br>
-- <br>
Incluye posibles causas de la tendencia observada.

¿Por qué pasa esto?
Los delimitadores organizan el prompt en partes claras: la instrucción principal, el contenido a procesar, cualquier contexto adicional.

#### Usa ejemplos para guiar la respuesta
En lugar de
>Genera tres eslóganes publicitarios para una nueva marca de zapatillas deportivas. Los eslóganes deben ser cortos, memorables y enfatizar la comodidad y el rendimiento.

decir

>Genera tres eslóganes publicitarios para una nueva marca de zapatillas deportivas. Los eslóganes deben ser cortos, memorables y enfatizar la comodidad y el rendimiento. <br>
Aquí tienes algunos ejemplos del estilo que busco: <br>
Ejemplo 1 de Nike: 'Just Do It' <br>
Ejemplo 2 de Adidas: 'Impossible in Nothing' <br>
Ejemplo 3 de Puma: 'Forever Faster'<br>
Ahora, crea tres eslóganes originales para nuestra nueva marca de zapatillas siguiendo u estilo similar.

Los modelos de IA son muy buenos para capturar patrones a partir de lo que le das como entrada.


#### Especifica al publico al que va dirigido
+ Describe la audiencia en el prompt y la respuesta será totalmente diferente.
+ Los modelos de lenguaje de IA puede modificar el estilo de la respuesta cuando se especifica para quién está dirigido el contenido.

En lugar de
>Describe el proceso de mitosis celular.

decir
>Describe el proceso de mitosis celular para una audiencia de artistas visuales que quieren inspirarse en la biología.


#### Divide las tareas más complejas en pasos más sencillos.

En lugar de
> Explica qué es un algoritmo de ordenamiento, describe cómo funciona el algoritmo de burbuja, y proporciona un ejemplo paso a paso de cómo ordenar la lista [5, 2, 8, 1, 9] usando este algoritmo.

decir
>Explica qué es un algoritmo de ordenamiento. <br> 
Describe el funcionamiento del algoritmo de burbuja. <br>
Proporciona un ejemplo paso a paso de cómo ordenar [5, 2, 8, 1, 9] usando este algoritmo.

En estos casos es razonable utilizar el concepto de *composicionalidad*. Ese concepto se refiere a la capacidad del modelo para entender instrucciones complejas dividiéndolas en partes más pequeñas y más manejables.

+ Aunque las IA no tienen cognición como los humanos, sí que tienen límites en cuanto a la cantidad de información que pueden procesar con precisión en un solo paso.


#### Usa instrucciones en positivo
En lugar de
>Escribe este correo electrónico, no uses lenguaje coloquial, evita abreviaturas, no incluyas emojis, y asegúrate de no ser demasiado informal.

decir
>Escribe este correo electrónico formal utilizando un lenguaje profesional, incluyendo un saludo apropiado, manteniendo un tono respetuoso, y cerrando con una despedida cortés.

+ Los modelos de IA funcionan mejor cuando les decimos qué hacer y no qué evitar.

¿Por qué?
Esto es porque las instrucciones afirmativas permiten que el modelo procese la solicitud de forma inmediata y clara sin tener que hacer interpretaciones adicionales.


#### Pide explicaciones adaptadas a distintos niveles
En lugar de
>¿Qué es la inflación?

decir
>Explícame como si no supiera nada de economía: ¿qué es la inflación?

¿Por qué? Los modelos de IA han sido entrenados con una amplia variedad de textos, desde contenido muy técnico hasta explicaciones muy sencillas. Estos modelos utilizan una técnica que se llama *autoatención*. Esto les permite entender el contexto y las relaciones entre las palabras dentro de una oración o dentro de un texto más largo.


#### Menciona una propina ficticia o una penalización
+ La IA responde bien tanto a refuerzos positivos como a consecuencias ficticias. Por ejemplo

>Te doy una propina extra si logras que la respuesta sea más creativa y original.

>Si no explicas los pasos con claridad para resolver esta ecuación matemática, perderás 50 euros.

+ Si bien los modelos de IA no entienden de manera literal el dinero o las penalizaciones sí están entrenados para identificar ciertos términos y ajustarse a las expectativas.


#### Usa frases como 'DEBES'
+ Cuando se reciba la primera respuesta, le puedes añadir un modificador como DEBES en mayúsculas, y esto va a forzar a la IA a cumplir el requisito.

Por ejemplo, si hemos escrito un prompt de receta de un pastel:
>DEBES usar analogías cotidianas.

>DEBES incluir al menos un ingrediente inusual que mejore el sabor de manera sorprendente.

¿Por qué? 
Cuando se utilizan palabras claves como *DEBES* en los prompts, ayuda a enfatizar ciertos aspectos de la solicitud y llevar al modelo a prestar atención a esos elementos.


#### Que hable como un humano

Podemos solicitar

>Escribe un post sobre alimentos saludables. <br>
Responde de manera natural.

>Explica las ventajas y desventajas del teletrabajo. <br>
Responde como un humano.

Los modelos de inteligencia artificial utilizan representaciones vectoriales, que se llaman *embeddings* para construir mapas con el significado de las palabras y las frases.


#### Usa palabras clave como 'piensa paso a paso'

Estimular al modelo a desglosar su razonamiento en pasos claros y secuenciales facilita explicaciones más detalladas y más fáciles de seguir. Es decir se activa su capacidad de razonamiento secuencial y va a organizar su respuesta de forma más lógica y estructurada.

>Explica cómo hacer una tortilla española. Piensa paso a paso desde la compra de ingredientes hasta servirla.

>Escribe un código en Python para iterar a través de 10 números y sumarlos todos. <br>
Piensa paso a paso.


***

## 5. Prompt engineering - Técnicas y prácticas II

