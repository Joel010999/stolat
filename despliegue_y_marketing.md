# Plan de Escalado STO LAT: Deploy & Marketing

## 1. Instrucciones de Despliegue en Netlify (Producción)
Actualmente, el proyecto está completamente refactorizado, "Mobile First", y optimizado para SEO local.
Sigue estos pasos para hacer el despliegue final (Deploy):

1. **Asegurar el Repositorio de GitHub**:
   Ya se arreglaron los conflictos. El código en tu rama local es el definitivo. Sube tus últimos cambios desde la terminal (que ya hicimos):
   ```bash
   git add .
   git commit -m "feat: Integración de SEO, Candy Cocktails y Estética Premium"
   git push origin main
   ```

2. **Deploy Automático en Netlify**:
   - Ingresa a tu panel de **Netlify**.
   - Si tu proyecto de GitHub (`Joelo010999/stolat`) ya está enlazado a `https://sto-lat.netlify.app/`, Netlify detectará el *push* a la rama `main` y automáticamente comenzará a hacer el build y a publicar los cambios.
   - En unos segundos, el estado cambiará a "Published".
   - *Nota*: Como el stack es HTML/CSS/JS nativo, no necesitas configurar comandos de build (`npm run build`). Deja el *Build command* en blanco y el *Publish directory* como `/` (o la carpeta raíz por defecto).

3. **Verificación de Performance**:
   - Accede a `https://sto-lat.netlify.app/`
   - Revisa la carga rápida de las imágenes de Candy Cocktails y el correcto ruteo a WhatsApp y Apps de Delivery. El SEO ya está activo.

---

## 2. Sugerencia de Copy para Lanzamiento en Instagram
Para alcanzar el impacto y tickets promedio para el objetivo mensual, implementaremos un *Copy* enfocado en FOMO (Fear of Missing Out), estética y comodidad.

**Imagen/Reel sugerido:**
Un video dinámico alternando nuestra fachada nocturna neon, un cliente riéndose con una botella premium, y un primer plano súper "aesthetic" del *Cotton Candy Fizz* (el trago del algodón de azúcar) preparándose.

**Texto (Caption) para Instagram:**
> 🍸 Golosinas, tragos de autor y la mejor bodega de Jujuy, ahora a un tap de distancia. 
> 
> Rediseñamos STO LAT para que el mejor momento de la semana comience desde tu celular. ¿Qué vas a encontrar en nuestra nueva tienda online?
> 
> ✨ **NEW: CANDY COCKTAILS**. Nuestra nueva locura en barra: Gin Paff, Cotton Candy Fizz, Lollipop Martini... Tus golosinas de la infancia convertidas en tragos de alta coctelería para tu feed.
> 📱 **Delivery Rápido**: Sumamos botones de acceso directo. ¿Pedís con WhatsApp, PedidosYa o Rappi? Vos elegís, nosotros armamos la previa.
> 📍 **Ubicaciones en vivo**: Encontrá tu sucursal más cercana en nuestro mapa interactivo. 
> 
> Siempre es buen momento para brindar. 🥂
> 👉 Etiquetá a tu amigo/a que siempre dice que "hoy no sale" para tentarlo con un buen Gomi-Ron Blue.
> 
> 🔗 Link en bio para conocer la carta y hacer tu pedido.
> 
> #StoLat #TragosDeAutor #CandyCocktails #CocteleriaJujuy #Previa #DrinksAesthetic #Jujuy

---
**Estrategia extra del consultor:** Usa este posteo y gástale algo de pauta publicitaria (Ads) en radio de 5km alrededor de las sucursales con el objetivo de "Tráfico al sitio web". Los botones de WhatsApp directos convertirán muy rápido.
