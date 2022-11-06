<script setup lang="ts">
import OGModule from './modules/OGModule';

const ogModule: OGModule = new OGModule('', '', '');

const match = /^#(?:[0-9a-fA-F]{3}){1,2}$/;

// @TODO: Move URL to .env
const url: string = 'http://localhost:6969';

function copy() {
  const newURL = `${url}/embed?color=${ogModule.color.replace('#', '')}&title=${
    ogModule.title
  }&description=${ogModule.description}`;

  navigator.clipboard.writeText(newURL);
}

// @TODO: Make text field with url next to copy button -> [URL Here] (copy)
function create() {
  ogModule.title = ogModule.title.replaceAll(' ', '%20');
  ogModule.description = ogModule.description.replaceAll(' ', '%20');

  const parent = document.getElementById('form');

  if (!document.getElementById('copy')) {
    const copyButton = document.createElement('button');
    copyButton.type = 'button';
    copyButton.className = 'secondary';
    copyButton.id = 'copy';
    copyButton.innerText = 'Copy URL to Clipboard';
    copyButton.addEventListener('click', () => {
      copy();
    });

    parent?.appendChild(copyButton);
  }
}

function validate() {
  const matchColor: boolean =
    ogModule.color !== '' && match.test(ogModule.color);

  const matchTitle: boolean =
    ogModule.title !== '' && ogModule.title.length <= 64;

  const matchDesc: boolean =
    ogModule.description !== '' && ogModule.description.length <= 1024;

  document
    .getElementById('color')
    ?.setAttribute('aria-invalid', `${!matchColor}`);

  document
    .getElementById('title')
    ?.setAttribute('aria-invalid', `${!matchTitle}`);

  document
    .getElementById('desc')
    ?.setAttribute('aria-invalid', `${!matchDesc}`);

  if (matchColor && matchTitle && matchDesc) {
    create();
  }
}
</script>

<template>
  <main class="container panel">
    <h1 class="center">Create Your Custom Embed</h1>
    <form id="form" @submit.prevent="validate()">
      <div class="grid">
        <label for="color">
          Color
          <input v-model="ogModule.color" id="color" type="color" />
        </label>

        <label for="title">
          Title
          <input
            v-model="ogModule.title"
            type="text"
            id="title"
            maxlength="64"
            placeholder="Cool Title!"
          />
        </label>
      </div>
      <label for="desc">Description</label>
      <input
        v-model="ogModule.description"
        type="text"
        id="desc"
        maxlength="1024"
        placeholder="Cool Description :D!"
      />

      <button type="submit">Create!</button>
    </form>
  </main>
</template>

<style scoped>
h1 {
  padding-top: 4rem;
}
</style>
