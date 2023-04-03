import pygame
from support import import_folder


class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'flame': import_folder('graph/particles/flame/frames'),
            'aura': import_folder('graph/particles/aura'),
            'heal': import_folder('graph/particles/heal/frames'),

            # attacks
            'claw': import_folder('graph/particles/claw'),
            'slash': import_folder('graph/particles/slash'),
            'sparkle': import_folder('graph/particles/sparkle'),
            'leaf_attack': import_folder('graph/particles/leaf_attack'),
            'thunder': import_folder('graph/particles/thunder'),

            # monster deaths
            'squid': import_folder('graph/particles/smoke_orange'),
            'Boss': import_folder('graph/particles/raccoon'),
            'spirit': import_folder('graph/particles/nova'),
            'bamboo': import_folder('graph/particles/bamboo'),

        }

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups) -> None:
        super().__init__(groups)

        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
