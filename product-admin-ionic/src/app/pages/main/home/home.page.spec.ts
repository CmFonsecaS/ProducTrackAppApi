import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { HomePage } from './home.page';
import { IonicModule } from '@ionic/angular';
import { AngularFireModule } from '@angular/fire/compat';
import { AngularFireAuthModule } from '@angular/fire/compat/auth';
import { FirebaseService } from 'src/app/services/firebase.service';

// Configuración de Firebase específica
const firebaseConfig = {
  apiKey: "AIzaSyAx4p_Bt3x1ETrSg423dW4GN671fXW9SrU",
  authDomain: "product-admin-app-16d8b.firebaseapp.com",
  projectId: "product-admin-app-16d8b",
  storageBucket: "product-admin-app-16d8b.appspot.com",
  messagingSenderId: "449307179096",
  appId: "1:449307179096:web:8541135b93268c90ba722d"
};

describe('HomePage', () => {
  let component: HomePage;
  let fixture: ComponentFixture<HomePage>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ HomePage ],
      imports: [
        IonicModule.forRoot(),
        AngularFireModule.initializeApp(firebaseConfig), // Importa y configura AngularFire
        AngularFireAuthModule
      ],
      providers: [ FirebaseService ]
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

