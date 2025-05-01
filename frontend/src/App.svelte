<script lang="ts">
  import { onMount } from 'svelte';

  let apiKey: string = '';

  onMount(async () => {
    try {
      const res = await fetch('/api/key');
      const data = await res.json();
      apiKey = data.apiKey;
      let url = `https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=${apiKey}`;

    } catch (error) {
      console.error('Failed to fetch API key:', error);
    }
  });
</script>

<main>


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
