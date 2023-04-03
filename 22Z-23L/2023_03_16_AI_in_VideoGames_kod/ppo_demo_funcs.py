import torch
import torch.nn as nn
class Categorical():
    pass
def softmax(stuff):
    pass
def calculate_returns(rewards, discount_factor, normalize = True):
    
    returns = []
    R = 0
    
    for r in reversed(rewards):
        R = r + R * discount_factor
        returns.insert(0, R)
        
    returns = torch.tensor(returns)
    
    if normalize:
        returns = (returns - returns.mean()) / returns.std()
        
    return returns

def calculate_advantages(returns, values, normalize = True):
    
    advantages = returns - values
    
    if normalize:
        
        advantages = (advantages - advantages.mean()) / advantages.std()
        
    return advantages

class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, dropout = 0.5):
        super().__init__()

        self.fc_1 = nn.Linear(input_dim, hidden_dim)
        self.fc_2 = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x):
        x = self.fc_1(x)
        x = self.dropout(x)
        x = nn.relu(x)
        x = self.fc_2(x)
        return x
    
not_done = True
nr_of_steps_per_simulation = 100
actor = MLP(1,1,1)
critic = MLP(1,1,1)
scene = Scene()
simulation_memory = []
discount_factor = 1
max_number_of_critic_iterations = 1
adam_optimizer = MLP(1,1,1)
clip_value = 0.2
threshold = 1
def train_actor():
    reward = 0
    simulation_memory = []
    for _ in range(nr_of_steps_per_simulation):
        observations = scene.get_next_state()
        actions = actor(observations)
        memory_value = critic(observations)
        actions_probabilities = softmax(actions)
        dist_actions = Categorical(actions_probabilities)
        action_taken = dist_actions.sample()
        log_prob_action = dist_actions.log_prob(action_taken)

        reward += scene.apply_action(action_taken)
        returns = calculate_returns(reward, discount_factor)

        gae = generalized_advantage_estimate = calculate_advantages(
                                                returns, memory_value)
        simulation_memory.append(
            [observations, action_taken, log_prob_action, returns, gae]
        )

        loss = (returns - memory_value)**2
        loss.backwards()
        adam_optimizer.step()

def train_critic(old_log_prob_actions):
    observations, actions_taken, log_prob_actions, returns, gaes = zip(*simulation_memory)

    for i in range(max_number_of_critic_iterations): 
        # Each time we are using ALL simulated frames
        policy_ratio = torch.exp(log_prob_actions - old_log_prob_actions) # division
        clipped_policy_ratio = policy_ratio.clamp(1 - clip_value, 1 + clip_value)
        policy_loss = policy_ratio * gaes
        clipped_policy_loss = clipped_policy_ratio * gaes

        final_loss = -torch.min(policy_loss, clipped_policy_loss).mean()
        final_loss.backwards()
        adam_optimizer.step()

        k1_div = (old_log_prob_actions - log_prob_actions).mean()
        if k1_div > threshold or k1_div < -threshold:
            break
 