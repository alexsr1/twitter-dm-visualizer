<script>
  export let messages;
  
  function decodeHtmlEntities(text) {
    const textarea = document.createElement('textarea');
    textarea.innerHTML = text;
    return textarea.value;
  }
  
  function getReactionEmoji(reactionKey) {
    const reactionMap = {
      'heart': '❤️',
      'laugh': '😂',
      'wow': '😮',
      'cry': '😢',
      'fire': '🔥',
      'thumbs_up': '👍',
      'thumbs_down': '👎',
      'emoji': '❤️', 
    };
    return reactionMap[reactionKey] || '👍'; 
  }
</script>

<div class="chat-container">
  {#each messages as msg}
    <div class="bubble {msg.senderId === messages[0].senderId ? 'me' : 'them'}">
      <p>{decodeHtmlEntities(msg.text || '')}</p>

      {#if msg.mediaUrls && msg.mediaUrls.length > 0}
        {#each msg.mediaUrls as media}
          {#if media.includes('.mp4')}
            <video 
              controls 
              preload="none"
              width="240"
              poster=""
            >
              <source src={`/categorized_media/${msg.senderId}/${msg.id}-${media.split('/').pop().split('?')[0]}`} type="video/mp4">
              <p>Your browser doesn't support video playback.</p>
            </video>
          {:else}
            <img 
              src={`/categorized_media/${msg.senderId}/${msg.id}-${media.split('/').pop().split('?')[0]}`} 
              width="240" 
              loading="lazy"
              alt="Media content"
            />
          {/if}
        {/each}
      {/if}

      <div class="timestamp">{new Date(msg.createdAt).toLocaleString()}</div>

      {#if msg.reactions && msg.reactions.length > 0}
        <div class="reactions">
          {#each msg.reactions as reaction}
            <span class="reaction" title="Reaction by {reaction.senderId} at {new Date(reaction.createdAt).toLocaleString()}">
              {getReactionEmoji(reaction.reactionKey)}
            </span>
          {/each}
        </div>
      {/if}
    </div>
  {/each}
</div>

<style>
  .chat-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }
  
  .bubble {
    max-width: 70%;
    padding: 0.75rem;
    border-radius: 1rem;
    position: relative;
  }
  
  .bubble.me {
    background: #007bff;
    color: white;
    align-self: flex-end;
    margin-left: auto;
  }
  
  .bubble.them {
    background: #f1f1f1;
    color: black;
    align-self: flex-start;
  }
  
  .bubble p {
    margin: 0 0 0.5rem 0;
  }
  
  .bubble img, .bubble video {
    border-radius: 0.5rem;
    margin: 0.5rem 0;
    max-width: 100%;
    height: auto;
  }
  
  .timestamp {
    font-size: 0.75rem;
    opacity: 0.7;
    margin-top: 0.5rem;
  }
  
  .reactions {
    display: flex;
    gap: 0.25rem;
    margin-top: 0.5rem;
    flex-wrap: wrap;
  }
  
  .reaction {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    padding: 0.25rem 0.5rem;
    font-size: 0.9rem;
    cursor: default;
    border: 1px solid rgba(255, 255, 255, 0.3);
  }
  
  .bubble.them .reaction {
    background: rgba(0, 0, 0, 0.1);
    border-color: rgba(0, 0, 0, 0.2);
  }
</style>