<script setup lang="ts">
// @TODO: move it to ./modules/OGModule.ts
// @TODO: Also rename this to OGModule
class Embed {
  constructor(
    public color: string,
    public title: string,
    public description: string
  ) {
    this.color = color;
    this.title = title;
    this.description = description;
  }
}

const embed = new Embed('', '', '');

const match = /^#(?:[0-9a-fA-F]{3}){1,2}$/;

// @TODO: Add a link component
function create() {
  // eslint-disable-next-line no-console
  console.log(embed);
}

function validate() {
  const matchColor: boolean = embed.color !== '' && match.test(embed.color);
  const matchTitle: boolean = embed.title !== '' && embed.title.length <= 64;
  const matchDesc: boolean =
    embed.description !== '' && embed.description.length <= 1024;

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
        <label for="color"
          >Color
          <input v-model="embed.color" id="color" type="color" />
        </label>

        <label for="title"
          >Title
          <input
            v-model="embed.title"
            type="text"
            id="title"
            maxlength="64"
            placeholder="Cool Embed!"
          />
        </label>
      </div>
      <label for="desc">Description</label>
      <input
        v-model="embed.description"
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
