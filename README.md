Proyecto Individual n°2 

Alumno Renzo Sosa

Aclaración inicial: 
      La computadora con la que se estaba realizando el trabajo se crasheo aproximadamente a las 15:00 horas del día 28/03 mientras se intentaba deployar en streamlit
por lo que quedo una version de prueba en github, versión que contenía el el archivo main.py, requirements y una carpeta visualizaciones la cual posteriormente se eliminó.

     El portfolio que aparece en el main py fue el que arrojó el analisis, cuestión muy distinta al EDA que posteriormene se subió ya que no recuerdo exactamente como 
hice el código que se quedó en la computadora crasheada. Dicha computadora que use para subir el readme actual y el EDA, poseen windows 7 por lo que no se puede usar visual
studio code, si utilicé google colab para realizar un bosquejo de lo que había sido el EDA el cual recomendó el portfolio que aparece en el main.py.
      
      Por último dicha computadora no me está dejando subir archivos a un repositorio nuevo, si subir a traves de arrastre a un repositorio preexistente, investigando parece ser una cuestion 
del certificado SSL. Dicho esto, procedo a explicar el trabajo.
      
      Para el desarrollo de este trabajo no se utilizo el concepto de correlación, concepto bastante importante a la hora del armado del portfolio. Por otro lado si se utilizó el concepto de ratio de sharpe y frontera de eficiencia de Markowitz, la cual recomiendo el portfolio de mercado. El portfolio creado por Markowitz brinda, dado un universo existente otorgado, la proporción exacta de cada elemento del universo otorgado para minimizar la volatilidad y maximizar el ratio de sharpe. En dicha
recomendación puede pasar que queden fuera elementos del universo otorgado.
      
      Para llegar al universo otorgado se sortearon las 10 acciones por ratio de sharpe, tambien previamente por una cuestión de curiosidad, se investigó cuales eram los sectores con mejor Sharpe, cuestión que no influyó en el armado final de portfolio. Una vez sorteados las acciones con mejor Sharpe, se eliminaron aquellas con una 
duración menor a 5 años de cotización y recién ahi se tomo aquellas 10 con mejor Sharpe. Por que se hizo esto? Primeramente por falta de datos a la hora de cotizar, segundoporque tampoco se puede observar su beta y tercero, y esto queda a discreción dela autor, tienen mejor Sharpe, pero obviamente un Sharpe con menos datos debido a la carencia de ruedas de cotizaciones.
      
      Otro factor importante a resalta es que el portfolio aquí obtenido no tiene en cuenta la existencia de la tasa libre de riesgo, a la vez que solamente es un portfolio
armado por elementos de renta variable. La risk free o tasa libre de riesgo tiene un papel fundamental en el armado de portfolios, ya sea cuando aumenta provocando esto una reorganización de los portfolios, vendiendo activos de renta variable para aumentar la posición de activos de renta fija, como cuando la misma baja desincentivando la inversión en activos de renta variable a la vez que favorece el apalancamiento, es decir me endedudo para aumentar la proporción de renta variable en m cartera.En simples palabras la rf es una cuestión fundamental a la hora de armar portfolios.
     
     Otra cuestión interesante es que el portfolio recomendado es para un cliente poco averso al riesgo, en el sentido que se le está recomendando una canasta de activos de renta variable, independedientemente que se haya escogido aquellas acciones que minimizan la volatilidad. Por lo general la volatilidad de los activos libres de riesgo suele ser menor a la de un activo de renta variable, inclusive teniendo en cuenta que dicho activo sea un etf de activos de renta variable. 
     
