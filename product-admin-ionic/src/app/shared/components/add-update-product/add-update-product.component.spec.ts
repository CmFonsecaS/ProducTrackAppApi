import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';
import { AngularFireModule } from '@angular/fire/compat';
import { AngularFireAuthModule } from '@angular/fire/compat/auth';
import { AddUpdateProductComponent } from './add-update-product.component';
import { FirebaseService } from 'src/app/services/firebase.service';

// Mock de la configuración de Firebase
const firebaseConfig = {
  apiKey: "AIzaSyAx4p_Bt3x1ETrSg423dW4GN671fXW9SrU",
  authDomain: "product-admin-app-16d8b.firebaseapp.com",
  projectId: "product-admin-app-16d8b",
  storageBucket: "product-admin-app-16d8b.appspot.com",
  messagingSenderId: "449307179096",
  appId: "1:449307179096:web:8541135b93268c90ba722d"
};

describe('AddUpdateProductComponent', () => {
  let component: AddUpdateProductComponent;
  let fixture: ComponentFixture<AddUpdateProductComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ AddUpdateProductComponent ],
      imports: [
        IonicModule.forRoot(),
        AngularFireModule.initializeApp(firebaseConfig),
        AngularFireAuthModule
      ],
      providers: [ FirebaseService ]
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddUpdateProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // Aumentar el tiempo de espera predeterminado de Jasmine
  jasmine.DEFAULT_TIMEOUT_INTERVAL = 10000; // 10 segundos

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

