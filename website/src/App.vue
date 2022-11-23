<script setup lang="ts">
const baseUrl: string = import.meta.env.VITE_URL;

async function create(submitEvent: any) {
  const { elements } = submitEvent.target;
  const { color, title, url, desc, image, small } = elements;

  // @TODO: Handling response status codes.
  // @TODO: Add aria-invalid for certain inputs
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
  );
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
    </form>
  </main>
</template>

<style scoped>
h1 {
  padding-top: 4rem;
}
</style>
