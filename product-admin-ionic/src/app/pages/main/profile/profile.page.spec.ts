import { ProfilePage } from './profile.page';
import { IonicModule } from '@ionic/angular';
import { AngularFireModule } from '@angular/fire/compat';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import { ModalController } from '@ionic/angular';
import { ComponentFixture, TestBed } from '@angular/core/testing';

// Configuración de Firebase específica
const firebaseConfig = {
  apiKey: "AIzaSyAx4p_Bt3x1ETrSg423dW4GN671fXW9SrU",
  authDomain: "product-admin-app-16d8b.firebaseapp.com",
  projectId: "product-admin-app-16d8b",
  storageBucket: "product-admin-app-16d8b.appspot.com",
  messagingSenderId: "449307179096",
  appId: "1:449307179096:web:8541135b93268c90ba722d"
};

// Mock de ModalController
class ModalControllerMock {}

describe('ProfilePage', () => {
  let component: ProfilePage;
  let fixture: ComponentFixture<ProfilePage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfilePage ],
      imports: [
        IonicModule.forRoot(),
        AngularFireModule.initializeApp(firebaseConfig),
      ],
      providers: [
        AngularFireAuth,
        { provide: ModalController, useClass: ModalControllerMock } // Provee el mock de ModalController
      ]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfilePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
















