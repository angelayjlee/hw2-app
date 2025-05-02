<script lang="ts">
  import { onMount } from 'svelte';

  let apiKey: string = '';
  let articles: any[] = [];
  let currentDate: string = '';

  function getCurrentDate(): string {
    const today = new Date();
    const options: Intl.DateTimeFormatOptions = {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    };
    return today.toLocaleDateString('en-US', options); // "Wednesday, May 1, 2025"
  }

  onMount(async () => {
    currentDate = getCurrentDate();
    await fetchArticles();
    try {
      const res = await fetch('http://localhost:8000/api/key'); //make request to backend for api key
      const data = await res.json(); //parse response as json
      apiKey = data.apiKey; //store api key
    } catch (error) { //call function to fetch articles after api key is retrieved 
      console.error('Failed to fetch API key:', error);
    }
  });

  //Function to fetch articles from the NYT API (backend)
  const fetchArticles = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/articles'); //make request to backend for articles
      const data = await res.json(); //parse response as json
      articles = data.articles; //store articles
      console.log("First article's multimedia:", articles[0].multimedia); //log first article's multimedia
    } catch (error) { //handle error
      console.error('Failed to fetch articles:', error);
    }
  };


</script>



<main>



  <header>
    <h1 class="logo">The New York Times</h1>
    <div class="date-header">
      <div class="date">{currentDate}</div>
      <div class="today-label">Today's Paper</div>
    </div>
    <hr class="headline-divider">
  </header>

  <div class="content">
    <section class="column 1">
      {#each articles.slice(0, 3) as article}
        <article class="article">
          <h2>{article.title}</h2>
          <p>{article.abstract}</p>

          {#if article.multimedia && article.multimedia.default}
          <img src={article.multimedia.default.url} alt={article.title} />
          {/if}

          <p class="meta">5 min read</p>

          {#if article.web_url}
          <a href={article.web_url} target="_blank" rel="noopener noreferrer" class="readMore-link">
          read full article
          </a>
          {:else}
          <p>No URL available</p>
        {/if}

        <hr />
        </article>
      {/each}
    </section>

    <section class="column 2">
      {#each articles.slice(3, 5) as article}
        <article class="article">
          <h2>{article.title}</h2>
          <p>{article.abstract}</p>

          {#if article.multimedia && article.multimedia.default}
          <img src={article.multimedia.default.url} alt={article.title} />
          {/if}

          <p class="meta">5 min read</p>
  
          {#if article.web_url}
          <a href={article.web_url} target="_blank" rel="noopener noreferrer" class="readMore-link">
          read full article
          </a>
          {:else}
          <p>No URL available</p>
        {/if}

        <hr />
        </article>
      {/each}
    </section>

    <section class="column 3">
      {#each articles.slice(5, 7) as article}
        <article class="article">
          <h2>{article.title}</h2>
          <p>{article.abstract}</p>

          {#if article.multimedia && article.multimedia.default}
          <img src={article.multimedia.default.url} alt={article.title} />
          {/if}

          <p class="meta">5 min read</p>
         
          {#if article.web_url}
          <a href={article.web_url} target="_blank" rel="noopener noreferrer" class="readMore-link">
          read full article
          </a>
          {:else}
          <p>No URL available</p>
        {/if}

        <hr />
        </article>
      {/each}
    </section>
  </div>

  <footer>
    <div class="footer-content">
      <p>ChatGPT MLA Citation: OpenAI. "Prompt." *ChatGPT*, 15 Apr. 2025, chat.openai.com/chat.  
        — "Response."
      </p>
      <p>HTML Citation: W3Schools. "HTML Tutorial." *W3Schools*, 2025</p>
      <p>CSS Citation: W3Schools. "CSS Tutorial." *W3Schools*, 2025</p>
    </div>
  </footer>



   <!-- Add HTML here -->
<!-- 
    <div class="header-container">
      <div class="item1">
        <div class="todays-date">Wednesday, April 16, 2025</div>
        <div class="todays-paper">Today's Paper</div>
      </div>

      <div class="spacer"> </div> 

      <div class="logo">
        <img src="NYTlogo.png" alt="New York Times" width="300" height="300">
      </div>
    </div>    
      

    <div class="grid-container">
      <div class="column" id="item-1">
        <img src="matcha.jpg" alt="Matcha" class="responsive-img" style="width:100px; height:auto;">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi.</p>
      </div>
      <div class="column" id="item-2">
        <h3>Headline 2</h3>
        <p>Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec velit neque.</p>    
      </div>

      <div class="column" id="item-3">
        <h3>Headline 3</h3>
        <p>Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Cras ultricies ligula sed magna dictum porta.</p>
      </div>

      // //Second row  
      <div class="column" id="item-4">
        <h3>Headline 4</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.</p>
      </div>
      <div class="column" id="item-5">
        <h3>Headline 5</h3>
        <p>Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet.</p>
      </div>
      <div class="column" id="item-6">
        <h3>Headline 6</h3>
        <p>Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta.</p>
      </div>
    </div>

    // Dark Horizontal Line Footer 
    <div class="footer"></div>
 -->


</main>

<style>

  
</style>
