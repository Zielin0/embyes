<script setup lang="ts">
const baseUrl: string = import.meta.env.VITE_URL;

async function create(submitEvent: any) {
  const { elements } = submitEvent.target;
  const { color, title, url, desc, image, small } = elements;

  const message = document.getElementById('message');

  let code: number;

  await fetch(
    `${baseUrl}/new?${new URLSearchParams({
      url: url.value,
      color: color.value.replace('#', ''),
      title: title.value,
      description: desc.value,
      image: image.value,
      small: small.value,
    })}`,
    {
      method: 'POST',
    }
  )
    .then((res) => {
      code = res.status;
      if (res.status < 300 && res.status > 200) {
        message!.setAttribute('style', 'color: #6de24d');
      } else {
        message!.setAttribute('style', 'color: #ef4543');
      }

      return res.text();
    })
    .then((text) => {
      if (code === 201) {
        // @TODO: Do created stuff info and copy button
      }
      if (code !== 429) {
        document
          .getElementById('title')
          ?.setAttribute('aria-invalid', `${title.value === ''}`);

        document
          .getElementById('url')
          ?.setAttribute('aria-invalid', `${url.value === '' || code === 409}`);

        document
          .getElementById('desc')
          ?.setAttribute('aria-invalid', `${desc.value === ''}`);

        message!.innerText = text;
      }
      message!.innerText = 'Too many requests';
    });
}
</script>

<template>
  <main class="container panel">
    <h1 class="center">Create Your Custom Embed</h1>
    <form id="form" @submit.prevent="create">
      <div class="grid">
        <label for="color">
          Color
          <input id="color" type="color" />
        </label>

        <label for="title">
          Title
          <input
            type="text"
            id="title"
            maxlength="64"
            placeholder="Cool Title!"
          />
        </label>

        <label for="url">
          Custom URL
          <input
            type="text"
            id="url"
            maxlength="48"
            placeholder="goofy-embed"
          />
        </label>
      </div>

      <label for="desc">Description</label>
      <input
        type="text"
        id="desc"
        maxlength="256"
        placeholder="Cool Description :D!"
      />

      <div class="grid">
        <label for="image">
          Image URL
          <input
            type="text"
            id="image"
            maxlength="128"
            placeholder="example.com/image.png"
          />
        </label>

        <label for="small">
          Small Text
          <input
            type="text"
            id="small"
            maxlength="32"
            placeholder="Hello Mom!"
          />
        </label>
      </div>

      <button type="submit">Create!</button>

      <span id="message"></span>
    </form>
  </main>
</template>

<style scoped>
h1 {
  padding-top: 4rem;
}
</style>
