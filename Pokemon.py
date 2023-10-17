state_scores = {
    'evet': self.update_max_event_rew_(),
    #'part_xp': 0.1*sum(poke_xps),
    'level': self.get_levels_reward(),
    'heal': self.total_healing_rew,
    'op_lvl': self.update_max_op_level(),
    'dead': -0.1*self.died_count,
    'badge': self.get_badges() * 2,
    #'op_poke': self.max_opponent_poke * 800,
    #'money': money * 3,
    #'seen_poke': seen_poke_count * 400,
    'explore': self.get
}
def read_m(self, addr):
    return self.pyboy.get_memory_value(addr)
def read_bit(self, addr, bit: int) -> bool:
    # add padding so zero will read '0b100000000' instead of '0b0'
    return bin(256 + self.read_m(addr)) [-bit-1] == '1'
def get_levels_sum(self):
    poke_levels = [
        max(self.read_m(a) - 2, 0)
        for a in [0xD18C, 0XD1B8 0XD210, 0XD23C, 0XD268]
    ]
    return max(sum(poke_levels)- 4, 0) #subtract starting pokemon level