<script>
  import { onMount } from 'svelte';
  import ChatView from './components/ChatView.svelte';

  let messagesByConversation = {};
  let selectedConversation = null;
  let loading = true;
  let error = null;

  onMount(async () => {
    try {
      const res = await fetch('/direct-messages.json');
      if (!res.ok) {
        throw new Error(`Failed to fetch: ${res.status}`);
      }
      const rawData = await res.json();

      const conversations = {};

      rawData.forEach(entry => {
        const conv = entry.dmConversation;
        if (!conv || !conv.conversationId) return; // Skip invalid entries
        
        const convId = conv.conversationId;
        if (conv.messages) {
          conv.messages.forEach(msg => {
            const message = msg.messageCreate;
            if (message) { // Make sure message exists
              if (!conversations[convId]) conversations[convId] = [];
              conversations[convId].push(message);
            }
          });
        }
      });

      // Sort messages in each conversation by creation time
      for (const convId in conversations) {
        conversations[convId].sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt));
      }

      messagesByConversation = conversations;
      loading = false;
    } catch (err) {
      console.error('Error loading messages:', err);
      error = err.message;
      loading = false;
    }
  });

  const handleSelect = (id) => {
    selectedConversation = id;
  };
</script>

<h1 class="title">Twitter DM Viewer</h1>

{#if loading}
  <p>Loading messages…</p>
{:else if error}
  <p>Error loading messages: {error}</p>
{:else if Object.keys(messagesByConversation).length}
  <div class="container">
    <aside class="sidebar">
      <h2>Conversations</h2>
      {#each Object.keys(messagesByConversation) as convId}
        <button on:click={() => handleSelect(convId)} class:selected={convId === selectedConversation}>
          {convId}
        </button>
      {/each}
    </aside>

    <main class="chat">
      {#if selectedConversation}
        <ChatView messages={messagesByConversation[selectedConversation]} />
      {:else}
        <p>Select a conversation to begin.</p>
      {/if}
    </main>
  </div>
{:else}
  <p>No conversations found.</p>
{/if}

<style>
  .title { text-align: center; margin: 1rem; }
  .container { display: flex; height: 90vh; }
  .sidebar {
    width: 250px;
    border-right: 1px solid #ccc;
    overflow-y: auto;
    padding: 1rem;
  }
  .sidebar button {
    display: block;
    margin-bottom: 0.5rem;
    width: 100%;
    text-align: left;
  }
  .sidebar button.selected {
    font-weight: bold;
    background: #eee;
  }
  .chat {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
  }
</style>