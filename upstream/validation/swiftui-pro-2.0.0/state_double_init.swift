import SwiftUI
struct Sample: View {
 @State private var count = 1
 init() { self.count = 2 }
 var body: some View { Text("\(count)") }
}
