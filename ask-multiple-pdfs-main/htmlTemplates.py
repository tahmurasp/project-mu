css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #FCFFCE
}
.chat-message.bot {
    background-color: #E2F7FF
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #000000;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/cute-robot-holding-clipboard-cartoon-vector-icon-illustration-science-technology-icon-isolated_138676-5184.jpg?t=st=1711267809~exp=1711271409~hmac=cfa2ed08c9b4ad0668b3c99e5a09f5d86496f029518a8eb275b576be75db97e2&w=740" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/businessman-character-avatar-isolated_24877-60111.jpg?t=st=1711268022~exp=1711271622~hmac=9117ee92a663c030ccd3ed47202ae1080b8abac471acf631e732e2786b01c1ce&w=740">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''