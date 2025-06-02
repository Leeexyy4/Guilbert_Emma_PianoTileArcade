import pygame
from ui.page.basePage import BasePage
from ui.utils.inputBox import InputBox

class InscriptionPage(BasePage):
    def __init__(self, windowManager):
        super().__init__(windowManager)
        font = self._windowManager.getFontSmall()
        color = self._windowManager.getColor()
        self.input_username = InputBox(0, 0, 280, 50, font, color.getGris(), color.getViolet())
        self.input_password = InputBox(0, 0, 280, 50, font, color.getGris(), color.getViolet())
        self.input_confirm = InputBox(0, 0, 280, 50, font, color.getGris(), color.getViolet())
        self.button_inscrire = pygame.Rect(0, 0, 280, 60)
        self.erreur_inscription = ""  # 🔴 Chaîne vide = pas d'erreur

    def affichagePage(self):
        window = self._windowManager.getWindow()
        font = self._windowManager.getFontSmall()
        font_title = self._windowManager.getFontTall()
        color = self._windowManager.getColor()
        blanc = color.getBlanc()
        violet = color.getViolet()
        noir = (0, 0, 0)

        screen_width = self._windowManager.getScreenWidth()
        screen_height = self._windowManager.getScreenHeight()

        form_width = 400
        form_height = 400
        form_x = (screen_width - form_width) // 2
        form_y = (screen_height - form_height) // 2

        pygame.draw.rect(window, color.getGris(), (form_x - 20, form_y - 40, form_width + 40, form_height + 120))

        titre = font_title.render("Inscription", True, noir)
        window.blit(titre, titre.get_rect(center=(screen_width // 2, form_y + 10)))

        spacing = 100
        input_x = form_x + (form_width - 280) // 2
        input_y = form_y

        labels = ["Nom d'utilisateur :", "Mot de passe :", "Confirmer le mot de passe :"]
        inputs = [self.input_username, self.input_password, self.input_confirm]

        for i in range(3):
            label = font.render(labels[i], True, noir)
            window.blit(label, (input_x, input_y + 60 + i * spacing))
            inputs[i].rect.topleft = (input_x, input_y + 90 + i * spacing)
            inputs[i].draw(window)

        self.button_inscrire.topleft = (input_x, input_y + 80 + 3 * spacing)
        pygame.draw.rect(window, violet, self.button_inscrire)
        txt = font.render("S'inscrire", True, blanc)
        window.blit(txt, txt.get_rect(center=self.button_inscrire.center))

        if self.erreur_inscription:
            erreur_txt = font.render(self.erreur_inscription, True, (255, 0, 0))
            window.blit(erreur_txt, (input_x, input_y + 80 + 4 * spacing))

    def handle_event(self, event):
        self.input_username.handle_event(event)
        self.input_password.handle_event(event)
        self.input_confirm.handle_event(event)
        self._windowManager.getInterface().setUpdate(True)
