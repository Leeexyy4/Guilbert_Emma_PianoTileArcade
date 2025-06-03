import pygame
from ui.page.basePage import BasePage

class HelpPage(BasePage):
    def affichagePage(self):
        screen = self._windowManager.getWindow()
        font = self._windowManager.getFontSmall()
        font_tall = self._windowManager.getFontTall()  # police pour les titres
        color = self._windowManager.getColor()
        button_descriptions = {
            "joueur1": {
                pygame.K_1: "Action 1",
                pygame.K_2: "Action 2",
                pygame.K_3: "Action 3",
                pygame.K_4: "Action 4",
                pygame.K_5: "Action 5",
                pygame.K_6: "Valider",
            },
            "joueur2": {
                pygame.K_KP1: "Action 1",
                pygame.K_KP2: "Action 2",
                pygame.K_KP3: "Action 3",
                pygame.K_KP4: "Action 4",
                pygame.K_KP5: "Action 5",
                pygame.K_KP6: "Valider",
            }
        }

        start_x_j1 = self._windowManager.getScreenWidth() // 2 - 400
        start_x_j2 = self._windowManager.getScreenWidth() // 2 + 100
        start_y = 300
        spacing_y = 60

        # Titres joueurs
        title_j1 = font_tall.render("Joueur 1", True, color.getBlanc())
        title_j2 = font_tall.render("Joueur 2", True, color.getBlanc())
        screen.blit(title_j1, (start_x_j1, start_y - 70))
        screen.blit(title_j2, (start_x_j2, start_y - 70))

        def draw_joystick_direction(surface, rect, direction, color_fg):
            pygame.draw.rect(surface, color_fg, rect, 3)
            cx, cy = rect.center
            offset = 12
            # Dessin simple de fleche selon direction
            if direction == "up":
                points = [(cx, cy - offset), (cx - 7, cy + 7), (cx + 7, cy + 7)]
            elif direction == "down":
                points = [(cx, cy + offset), (cx - 7, cy - 7), (cx + 7, cy - 7)]
            elif direction == "left":
                points = [(cx - offset, cy), (cx + 7, cy - 7), (cx + 7, cy + 7)]
            elif direction == "right":
                points = [(cx + offset, cy), (cx - 7, cy - 7), (cx - 7, cy + 7)]
            else:
                points = []
            if points:
                pygame.draw.polygon(surface, color_fg, points)

        # Pour chaque joueur, colonne gauche/droite
        for start_x, joueur in [(start_x_j1, "joueur1"), (start_x_j2, "joueur2")]:
            for i, (key, desc) in enumerate(button_descriptions[joueur].items()):
                y = start_y + i * spacing_y
                rect_button = pygame.Rect(start_x, y, 50, 50)

                # fond carre contour violet
                pygame.draw.rect(screen, color.getViolet(), rect_button, 3)

                # Pour les touches 1-4 : dessiner joystick direction
                if key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4]:
                    # Definir la direction selon touche
                    if key in [pygame.K_1, pygame.K_KP1]:
                        direction = "up"
                    elif key in [pygame.K_2, pygame.K_KP2]:
                        direction = "down"
                    elif key in [pygame.K_3, pygame.K_KP3]:
                        direction = "left"
                    elif key in [pygame.K_4, pygame.K_KP4]:
                        direction = "right"
                    else:
                        direction = None
                    draw_joystick_direction(screen, rect_button, direction, color.getBlanc())
                else:
                    # Sinon texte touche normal
                    key_name = pygame.key.name(key).upper().replace("[", "").replace("]", "")
                    key_text = font.render(key_name, True, color.getBlanc())
                    key_rect = key_text.get_rect(center=rect_button.center)
                    screen.blit(key_text, key_rect)

                # Description a droite
                desc_text = font.render(desc, True, color.getBlanc())
                screen.blit(desc_text, (start_x + 70, y + 15))
